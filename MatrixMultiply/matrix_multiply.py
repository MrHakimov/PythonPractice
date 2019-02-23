# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
import random as rd


def split_array(a, m, n, c):
    str_i = 0
    if n > m:
        arr1 = [[0] * m for i in range(m)]
        for i in range(c, c+m):
            stb_i = 0
            for j in range(m):
                arr1[str_i][stb_i] = a[i][j]
                stb_i += 1
            str_i += 1
    else:
        arr1 = [[0] * n for i in range(n)]
        for i in range(n):
            stb_i = 0
            for j in range(c, c+n):
                arr1[str_i][stb_i] = a[i][j]
                stb_i += 1
            str_i += 1

    return arr1


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
            for j in range(k,n):
                a12[i][p] = A[i][j]
                b12[i][p] = B[i][j]
                c12[i][p] = 0
                p += 1
        p = 0
        for i in range(k,n):
            for j in range(k):
                a21[p][j] = A[i][j]
                b21[p][j] = B[i][j]
                c21[p][j] = 0
            p1 = 0
            for j in range(k,n):
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

n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))
b = [[0] * m for i in range(n)]
a = [[0] * n for i in range(m)]
c=[]
for i in range(n):
    for j in range(m):
        a[j][i] = rd.randint(1, 10)
        b[i][j] = rd.randint(1, 10)
# a = [[1, 2], [3, 4], [5, 6],[7, 8]]
# b = [[1, 2, 3, 4], [5, 6, 7, 8]]
# n, m = 2, 4
print('a', a)
print('b', b)

for i in range(max(n, m)//min(m, n)):
    c += smmr(split_array(a, n, m, i * min(n, m)), split_array(b, m, n, i * min(n, m)))

print('C: ', c)
