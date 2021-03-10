import matplotlib.pyplot as plt
from installer import check_CPU, get_CPU, to_license_key


def main():
    mas = []
    c = 0
    f = open('x.txt', 'r')
    for i in f:
        i = i.split()
        for j in range(len(i)):
            mas.append(int(i[j]))
            c = c + 1

    print(c)
    ##for i in mas:
    ##    print(i)
        
    mas1 = []
    c = 0
    for i in range (len(mas)-1):
        mas1.append(mas[i+1] - mas[i])
        c += 1
    print(c)
    ##print(mas1)

    from collections import Counter
    mas2 = Counter(mas1)
    print()
    print(mas2)
    print('max = ', max(mas2))
    print('min = ', min(mas2))
    print(sum(mas2))
    plt.plot(mas[0:len(mas)-1], mas1)
    plt.show()



if __name__ == "__main__":
    is_have_license = check_CPU(get_CPU())

    if is_have_license:
        main()
    else:
        print("Sorry, access is denied!")
        choice = input("Do you want to install the app? [Y/N]: ")
        if choice == 'Y':
            to_license_key(get_CPU())
        else:
            exit()
