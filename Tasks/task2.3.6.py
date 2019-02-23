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

def Insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = binary_search_iteration(A[0:j],key)
        while j >= i:
            A[j] = A[j-1]
            j = j - 1
        A[i] = key
    return A

if s==1:
    print(A)
    print("="*k)
    print(Insertion_sort(A))
else:
    Insertion_sort(A)