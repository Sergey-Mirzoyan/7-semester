import haffman
import json
from bitarray import bitarray


def convert_bit_to_int(bits: bitarray):
    mes_num = []
    for i in range(len(bits) // 8):
        num = memoryview(bits[i * 8:(i + 1) * 8])
        mes_num.append(num[0])

    return mes_num
def write_file(filename, mes_bit: bitarray):
    file = open(filename, 'wb')
    mes_bit.tofile(file)
    file.close()
def main():
    x = 1
    while x == 1:
        mode = input("Enter mode(1 - encode, 2 - decode, 3 - exit) :")
        if mode == '1':
            print("Введите начальную строку: ")
            s = input()
            file_name = input('file name: ')
            file_extension = '.' + input('file extansion: ')

            mes_bit = bitarray()
            file = open(file_name+file_extension, 'rb')
            mes_bit.fromfile(file)
            file.close()
            
            f = open('enc_file.txt', 'w')
            mes_bit = convert_bit_to_int(mes_bit)
            code = haffman.huffman_encode(mes_bit)
            encoded = "".join(code[ch] for ch in mes_bit)
            print("Закодированная строка: ")
            print(encoded)
            f.write(encoded)
            f.close()
        elif mode == '2':
            with open('enc_file.txt', 'r') as f:
                encoded  = f.read()

            scode = haffman.huffman_decode(encoded)
            print("Получим закодированную строку: ")
            write_file(file_name + '_denc' + file_extension, scode)
        elif mode == '3':
            x = 0
        else:
            pass


if __name__ == "__main__":
    main()
