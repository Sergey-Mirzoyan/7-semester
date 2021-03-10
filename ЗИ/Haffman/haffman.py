import ast
import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")     # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, acc + "1")    # затем пойти в правого потомка, добавив к префиксу "1"


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"        # если строка длиной 1 то acc = "", для этого случая
                                            #         установим значение acc = "0"


def huffman_encode(s):
    h = []                                  # инициализируем очередь с приоритетами
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))  # очередь будет представлена частотой символа, счетчиком и самим символом
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}                               # инициализируем словарь кодов символов
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    with open('node.txt', 'w') as fw:
        fw.write('{0}'.format(code))
    return code


def huffman_decode(encoded):
    with open('node.txt') as fr:
        code = ast.literal_eval(fr.read())
    sx = []                                 # инициализируем массив символов раскодированной строки
    enc_ch = ""                             # инициализируем значение закодированного символа
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:  # постараемся найти закодированный символ в словаре кодов
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)
