# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
n = int(input("Количество строк: "))
a = [[0] * n for i in range(n)]
b = [[0] * n for i in range(n)]
c = [[0] * n for i in range(n)]

'''for i in range(n):
    for j in range(n):
        at = "Элемент массива, a[" + str(i) + ', ' + str(j) + ']: '
        bt = "Элемент массива, b[" + str(i) + ', ' + str(j) + ']: '
        a[i][j] = int(input(at))#random.randint(1, 10)
        b[i][j] = int(input(bt))#random.randint(1, 10)'''

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(a)
print(b)
for i in range(n):
    for j in range(n):
        c[i][j] = 0
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]
print(c)
