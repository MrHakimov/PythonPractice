# author: Muhammadjon Hakimov
from random import randint
from sys import argv
try:
    k = int(argv[1])
except:
    k = 10

a = [randint(1,100) for x in range(k)]

def merge(A,lo,hi):
    if lo < hi:
        m = int((lo + hi)/2)
        merge(a, lo, m)
        merge(a, m + 1, hi)
        b = a[lo:m + 1]
        c = a[m + 1:hi + 1]
        i = j = 0
        for k in range(lo,hi+1):
            if i < len(b)and (j == len(c) or b[i] < c[j]):
                a[k] = b[i]
                i = i + 1
            else:
                a[k] = c[j]
                j = j + 1

def merge_sort(a):
    merge(a, 0, len(a)-1)

print(a)
merge_sort(a)
print(a)
