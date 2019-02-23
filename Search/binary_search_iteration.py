# author: Muhammadjon Hakimov
#-*- coding: utf-8 -*-
from random import randint
from sys import argv
try:
    k = int(argv[1])
    s = int(argv[2])
except:
    k = 10
    s = 1
A = [x+1 for x in range(k)]

def binary_search_iteration(A,key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] >= key:
            right = middle
        else:
            left = middle
    return right
v = A[randint(1,k)]
if s == 1:
    print(A,v)
    print(binary_search_iteration(A,v))
else:
    binary_search_iteration(A,v)
