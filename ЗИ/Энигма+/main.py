from enigma_func import *

def get_reflector(n):
    reflector = n * [-1]
    temp_arr = [x for x in range(n)]

    while(len(temp_arr)):
        first = temp_arr.pop(randint(0, len(temp_arr) - 1))
        second = temp_arr.pop(randint(0, len(temp_arr) - 1))
        reflector[first] = second
        reflector[second] = first

    return reflector



def encode_char(ch, rotor_1, rotor_2, rotor_3, reflector):
    ch1 = rotor_1[ch]
    ch2 = rotor_2[ch1]
    ch3 = rotor_3[ch2]

    ch4 = reflector[ch3]

    ch5 = rotor_3.index(ch4)
    ch6 = rotor_2.index(ch5)
    ch7 = rotor_1.index(ch6)

    return ch7

def encode(input_arr, rotor_1, rotor_2, rotor_3, reflector):
    result = len(input_arr) * [-1]
    count_1 = 0
    count_2 = 0
    for ind in range(len(input_arr)):
        ch = input_arr[ind]
        result[ind] = encode_char(ch, rotor_1, rotor_2, rotor_3, reflector)
        rotor_1, rotor_2, rotor_3, count_1, count_2 = rotate_rotors(rotor_1, rotor_2, rotor_3, count_1, count_2)

    return result


N = 256

if __name__ == '__main__':
    rotor_1 = make_rot(N)
    rotor_2 = make_rot(N)
    rotor_3 = make_rot(N)
    reflector = get_reflector(N)


    file_name = str(input("Input name of file:"))
    try:
        file = open(file_name, 'rb')
        input_str = file.read()
        #input_bytes = str_to_bytes(input_str)

        

        result = ''
        flag = 1
        while  flag:
            print("1. encode\n2. decode")
            choice = input('>>> ')
            if choice == '1':
                result = encode(input_str, rotor_1, rotor_2, rotor_3, reflector)

                print("Input: ")
                print(bytes_to_str(input_str))

                print("Output: ")
                print(bytes_to_str(result),'\n')

            elif choice == '2':
                result_decode = encode(result, rotor_1, rotor_2, rotor_3, reflector)
            
                print("Input: ")
                print(bytes_to_str(result))
                print("Output: ")
                print(bytes_to_str(result_decode))
            elif choice == '3':
                print('exit')
                flag = 0
                file.close()

    except:
        print("File not found\n")
