#  author: Muhammadjon Hakimov
#  -*- coding: utf-8 -*-
def add(A, B):
    n = len(A[0])
    m = len(A)
    C = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def add_horizontal(a, b):
    n = len(a[0])
    c = [[0] * n * 2 for i in range(n)]
    for i in range(n):
        c[i] = a[i] + b[i]
    return c

import random as rd
global a, b, c
n = int(input("Количество строк: "))
a = [[0] * n for i in range(n)]
b = [[0] * n for i in range(n)]
c = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = rd.randint(1, 10)
        b[i][j] = rd.randint(1, 10)
# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# a=[[1, 2], [3, 4]]
# b=[[5, 6], [7, 8]]
# a=[[1, 2, 3, 4], [2, 0, 1, 3], [1, 1, 2, 0], [4, 1, 1, 4]]
# b=[[1, 0, 1, 2], [3, 1, 4, 2], [0, 2, 3, 1], [4, 3, 0, 2]]
# a=[[0, 1], [-2, -1]]
# b=[[2, 2], [7, 3]]
a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b=[[3, 4, 5], [7, 1, 8], [6, 9, 2]]
print('A:')
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end='\t')
    print()
print('B:')
for i in range(len(b)):
    for j in range(len(b[0])):
        print(b[i][j], end='\t')
    print()


def smmr(A, B):
    n = len(A[0])
    C = [[0] * n for i in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        m = int(n/2)
        a11 = [[0] * m for i in range(m)]
        a12 = [[0] * m for i in range(m)]
        a21 = [[0] * m for i in range(m)]
        a22 = [[0] * m for i in range(m)]
        b11 = [[0] * m for i in range(m)]
        b12 = [[0] * m for i in range(m)]
        b21 = [[0] * m for i in range(m)]
        b22 = [[0] * m for i in range(m)]
        c11 = [[0] * m for i in range(m)]
        c12 = [[0] * m for i in range(m)]
        c21 = [[0] * m for i in range(m)]
        c22 = [[0] * m for i in range(m)]
        k = (n - 1) // 2 + 1
        for i in range(k):
            for j in range(k):
                a11[i][j] = A[i][j]
                b11[i][j] = B[i][j]
                c11[i][j] = 0
            p = 0
            for j in range(k, n):
                a12[i][p] = A[i][j]
                b12[i][p] = B[i][j]
                c12[i][p] = 0
                p += 1
        p = 0
        for i in range(k, n):
            for j in range(k):
                a21[p][j] = A[i][j]
                b21[p][j] = B[i][j]
                c21[p][j] = 0
            p1 = 0
            for j in range(k, n):
                a22[p][p1] = A[i][j]
                b22[p][p1] = B[i][j]
                c22[p][p1] = 0
                p1 += 1
            p += 1
        c11 = add(smmr(a11, b11), smmr(a12, b21))
        c12 = add(smmr(a11, b12), smmr(a12, b22))
        c21 = add(smmr(a21, b11), smmr(a22, b21))
        c22 = add(smmr(a21, b12), smmr(a22, b22))
        p1 = add_horizontal(c11, c12)
        p2 = add_horizontal(c21, c22)
        C = p1+p2
    return C
c=smmr(a, b)
print('C:')
for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j], end='\t')
    print()
