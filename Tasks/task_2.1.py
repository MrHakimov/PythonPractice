# author: Muhammadjon Hakimov
from random import randint
from sys import argv
try:
    k = int(argv[1])
    s = int(argv[2])
except:
    k = 10
    s = 1
a = [randint(1,10000) for x in range(k)]

def Insertion_sort(A):
    #print('ISA',A)
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i-=1
        A[i+1]=key
    return A

def merge(a,p,q,r):
        b = Insertion_sort(a[p:q+1]) #a[p:q+1]
        c = Insertion_sort(a[q+1:r+1]) #a[q+1:r+1]
        i = j = 0
        for k in range(p,r+1):
            if i < len(b)and (j == len(c) or b[i] <= c[j]):
                a[k] = b[i]
                i = i + 1
            else:
                a[k] = c[j]
                j = j + 1

def merge_sort(a,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)
        #Insertion_sort(a)
if s==1:
    print(a)
    merge_sort(a,0,len(a)-1)
    print(a)
else:
    merge_sort(a,0,len(a)-1)
