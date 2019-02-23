# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
import random
def selection_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j + 1
        while i < len(A):
            if A[i] < key:
                k = key
                key = A[i]
                A[i] = k
            i=i+1

        A[j]=key
    return A
A=[]
for i in range(15):
    A.append(random.randint(0,1000))
    
# A = [2, 3, 56, 45, 33, 21, 0, 13, 1]
print(A)
print("=" * 40)
print(selection_sort(A))
