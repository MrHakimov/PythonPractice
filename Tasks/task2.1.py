# author: Muhammadjon Hakimov
from random import randint
from sys import argv
try:
    k = int(argv[1])
    s = int(argv[2])
except:
    k = 10
    s = 1

A = [randint(1,100) for x in range(k)]

def Insertion_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i-=1
        A[i+1]=key
    return A
if s == 1:
	print(A)
	print(Insertion_sort(A))
else:
        Insertion_sort(A)
