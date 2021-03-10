import random
import math
import argparse
import sys
import os

def rabinMiller(n):
     s = n-1
     t = 0
     while s&1 == 0:
         s = s//2
         t +=1
     k = 0
     while k<128:
         a = random.randrange(2,n-1)
         v = pow(a,s,n)
         if v != 1:
             i=0
             while v != (n-1):
                 if i == t-1:
                     return False
                 else:
                     i = i+1
                     v = pow(v,2,n)
         k+=2
     return True

def isPrime(n):
     lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
     if (n >= 3):
         if (n&1 != 0):
             for p in lowPrimes:
                 if (n == p):
                    return True
                 if (n % p == 0):
                     return False
             return rabinMiller(n)
     return False

def generateLargePrime(k):
     r=100*(math.log(k,2)+1) 
     r_ = r
     while r>0:
         n = random.randrange(2**(k-1),2**(k))
         r-=1
         if isPrime(n) == True:
             return n
     return -1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
    
def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    _, d, _ = egcd(e, phi)
    print(d, phi)
    if d < 0:
      d = phi + d
    print((d * e) % phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [str(pow(char, key, n)) for char in plaintext]
    return ';'.join(cipher)
    

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [pow(char, key, n) for char in ciphertext]
    return plain
    


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-e', '--filenameToEncode', nargs='+')
    parser.add_argument ('-d', '--filenameToDecode', nargs='+')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-l', '--length', help='2048 <= key length >= 10', required=True)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    n = int(namespace.length)
    if n < 10:
      print('length must be >= 10')
      exit()

    if n > 2048:
      print('length must be <= 2048')
      exit()

    way = 'e'
    private = ()  
    if (namespace.filenameToDecode is not None):
        filename = namespace.filenameToDecode[0]
        way = 'd'
        print('Enter secret exponent:')
        dd = int(input())
        print('Enter module:')
        mm = int(input())
        private = (dd, mm) 
    else:
        if (namespace.filenameToEncode is not None):
            filename = namespace.filenameToEncode[0]
        else:
            print("This is not a file")
            exit()

    input_path = os.path.abspath(filename)
    if not os.path.isfile(input_path):
      print('This is not a file')
      exit()
     

    # generate prime numbers
    p = -1
    while p == -1:
      p = generateLargePrime(n)
    q = -1
    while q == -1:
      q = generateLargePrime(n)

    if way == 'e':
      public, private = generate_keypair(p, q)
      print("Public key is ", public ," Private key is ", private)
      with open(input_path, 'rb') as f:
        data = f.read()
      crypted_data = []
      temp = []
      for byte in data:
        temp.append(byte)
      encrypted_msg = encrypt(public, temp)
      
      out_path = os.path.join(os.path.dirname(input_path) , 'enc_' + os.path.basename(input_path))
      with open(out_path, 'w') as ff:
        ff.write(encrypted_msg)
      print('All encrypt')
      f.close()
      ff.close()


    if way == 'd':
      with open(input_path, 'r') as f:
        data = f.read()
      temp = [int(i) for i in data.split(';')]
      
      decrypted_data = decrypt(private, temp)
      out_path = os.path.join(os.path.dirname(input_path) , 'dec_' + os.path.basename(input_path))

      with open(out_path, 'wb') as ff:
        ff.write(bytes(decrypted_data))
      print('All decrypt')
      f.close()
      ff.close()
