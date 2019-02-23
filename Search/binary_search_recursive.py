# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
from random import randint
from sys import argv

try:
    k = int(argv[1])
    s = int(argv[2])
except:
    k = 10
    s = 1

A = [i+1 for i in range(k)]

def binary_search(A, v, B):
    n = len(A)
    q = int(n/2)
    a = "NIL"
    if A[q] == v:
        a = B[q]
    elif q > 0:
        if A[q] > v:
            A = A[0:q]
            B = B[0:q]
        elif A[q] < v:
            A = A[q:n]
            B = B[q:n]
        a=binary_search(A, v, B)
    return a
B = [i for i in range(len(A))]

v = A[randint(0,k-1)]

if s == 1:
    print(A,v)
    print(binary_search(A, v, B))
else:
    binary_search(A, v, B)
