from random import shuffle, randint
from array import array
SIZE = 256
def string_maker(string):
    arr = len(string) * [-1]
    for ind in range(len(srting)):
        arr[ind] = ord(string[ind])
    return arr

def make_rot(size):
    rot = []
    for i in range(size):
        rot.append(i)
    shuffle(rot)
    return rot

def rotate(arr, num):
    return arr[num:] + arr[:num]

def rotate_rotors(rotor_1, rotor_2, rotor_3, count_1, count_2):
    rotor_1 = rotate(rotor_1, 1)
    count_1 += 1

    if count_1 == SIZE:
        count_1 = 0
        rotor_2 = rotate(rotor_2, 1)
        count_2 += 1

        if count_2 == SIZE:
            count_2 = 0
            rotor_3 = rotate(rotor_3, 1)

    return rotor_1, rotor_2, rotor_3, count_1, count_2

def bytes_to_str(arr):
    s = ""
    for ind in range(len(arr)):
        s += chr(arr[ind])
    return s
