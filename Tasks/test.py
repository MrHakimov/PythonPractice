# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
def multiply(a,b):
    c = [[0]*len(a[0]) for i in range(len(a))]
    n = len(a)
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
    return c
def plus(A, B):
    n = len(A[0])
    m = len(A)
    C = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C
def minus(A, B):
    n = len(A[0])
    m = len(A)
    C = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C
a11=[[0]]#[[1,2],[2,0]]
a12=[[1]]#[[3,4],[1,3]]
a21=[[-2]]#[[1,1],[4,1]]
a22=[[-1]]#[[2,0],[1,4]]
b11=[[2]]#[[1,0],[3,1]]
b12=[[2]]#[[1,2],[4,2]]
b21=[[7]]#[[0,2],[4,3]]
b22=[[3]]#[[3,1],[0,2]]
s1=minus(b12,b22)
s2=plus(a11,a12)
s3=plus(a21,a22)
s4=minus(b21,b11)
s5=plus(a11,a22)
s6=plus(b11,b22)
s7=minus(a12,a22)
s8=plus(b21,b22)
s9=minus(a11,a21)
s10=plus(b11,b12)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)
print(s10)
p1=multiply(a11,s1)
p2=multiply(s2,b22)
p3=multiply(s3,b11)
p4=multiply(a22,s4)
p5=multiply(s5,s6)
p6=multiply(s7,s8)
p7=multiply(s9,s10)
print('-'*60)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
