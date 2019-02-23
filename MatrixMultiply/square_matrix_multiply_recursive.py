# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
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
        # at = "Элемент массива, a["+str(i)+','+str(j)+']: '
        # bt = "Элемент массива, b["+str(i)+','+str(j)+']: '
        # a[i][j] = int(input(at))
        # b[i][j] = int(input(bt))
# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]
print(a)
print(b)
print(len(a[0]))
exit()
def smmr(A, B):
    try:
        n = len(A)
    except:
        n = 1
    C = [[0] * n for i in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        C[0][0] = smmr(A[0], B[0]) + smmr(A[0], B[0])
        C[0][1] = smmr(A[0], B[1]) + smmr(A[0], B[1])
        C[1][0] = smmr(A[1], B[0]) + smmr(A[1], B[0])
        C[1][1] = smmr(A[1], B[1]) + smmr(A[1], B[1])
    return C

print(smmr(a, b))