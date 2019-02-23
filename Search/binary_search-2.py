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
A = [randint(1,100) for x in range(k)]
def binary_search(A, v):
    n = len(A)
    q = int(n/2)
    a = "No"
    if A[q] == v:
        a = "Yes"
    elif q > 0:
        if A[q] > v:
            A = A[0:q]
        elif A[q] < v:
            A = A[q:n]
        a=binary_search(A,v)
    return a

v = A[randint(0,k-1)]
if s == 1:
    print(A,v)
    print(binary_search(A, v))
else:
    binary_search(A, v)
