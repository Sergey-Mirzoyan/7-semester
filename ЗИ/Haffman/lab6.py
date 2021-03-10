import haffman


def main():
    mode = int(input("Enter mode(1 - encode, 2 - decode) :"))
    if mode == 1:
        print("Введите начальную строку: ")
        s = input()
        f = open('enc_file.txt', 'w')

        code = haffman.huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        print("Закодированная строка: ")
        print(encoded)
        f.write(encoded)
        f.close()
    elif mode == 2:
        with open('enc_file.txt', 'r') as f:
            encoded  = f.read()

        scode = haffman.huffman_decode(encoded)
        print("Получим закодированную строку: ")
        print(scode)
    else:
        pass


if __name__ == "__main__":
    main()
