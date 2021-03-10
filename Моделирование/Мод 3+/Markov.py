import os
import sys
from time import *
from random import random
from prettytable import PrettyTable
from numpy import linalg

size = 10
TIME_DELTA = 1e-5


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(round(matrix[i][j], 4), end = '\t')
        print()

def mtrx (matrix):
    for i in range (size):
        tmp = []
        for j in range (size):
            if i != j:
                tmp.append(round(random(), 4))
            else:
                tmp.append(0.0000)
        matrix.append(tmp)
    return matrix

def create_table():
    table = PrettyTable()
    names = [""]
    for i in range(1, size + 1):
        names.append(str(i))
    table.field_names = names

    for i in range(size):
        tmp = [i + 1]
        tmp.extend(item for item in matrix[i])
        table.add_row(tmp)
    return table

def limit_P(matrix):
    n = len(matrix)
    tmp = []
    tmp2 = []
    for i in range(n):
        x = []
        if i != n-1:
            for j in range(n):
                if i == j:
                    x.append(-sum(matrix[i]) + matrix[i][i])
                else:
                    x.append(matrix[j][i])
            tmp.append(x)
        else:
            x = []
            for j in range(n):
                x.append(1)
            tmp.append(x)
    print()
    #print_matrix(tmp)
    for i in range(n):
        if i != n-1:
            tmp2.append(0)
        else:
            tmp2.append(1)
    #print("\ntmp")
    #print_matrix(tmp)
    #for i in range(n):
    #    print(tmp2[i], end='\t')
    return linalg.solve(tmp, tmp2).tolist()

def clarification(matrix, start_P):
    n  = len(matrix)
    return [TIME_DELTA * sum([-sum(matrix[i]) * start_P[j] if i == j
            else matrix[j][i] * start_P[j] for j in range(n)])
            for i in range(n)]


def time_interval(matrix, P):
    n = len(matrix)
    curr = 0.0
    EPS = 1e-3
    start_P = [1.0 / n for i in range(n)]
    curr_P = start_P.copy()
    stab_t = [0.0 for i in range(n)]
    while not all(stab_t):
        current_dps = clarification(matrix, start_P)
        for i in range(n):
            if not (stab_t[i] and abs(curr_P[i] - P[i]) <= EPS):
                stab_t[i] = curr
            curr_P[i] += current_dps[i]
            curr += TIME_DELTA
    return stab_t

if __name__ == '__main__':
    matrix = []
    matrix = mtrx(matrix)
    #print("Изначальная матрица")
    #print_matrix(matrix)
    #sleep(3)

    table = create_table()
    print(table)

    P = limit_P(matrix)
    intervals = time_interval(matrix, P)

    limit = PrettyTable()
    limit.field_names = ["", "Предельные вероятности", "Время пребывания в ПС"]
    for i in range(size):
        tmp = [i + 1, round(P[i], 4), round(intervals[i], 4)]
        limit.add_row(tmp)
    print()
    print(limit)
    sleep(3)
