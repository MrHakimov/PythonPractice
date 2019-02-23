# author: Muhammadjon Hakimov
from random import randint
from sys import argv
try:
    k = int(argv[1])
except:
    k = 10

A = [randint(1, 100) for x in range(k)]

def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = int(len(A) / 2)
    # n1 = len(A[:middle])
    # n2 = len(A[middle:])
    L = A[:middle] # [A[x] for x in range(n1)]
    R = A[middle:] # [A[middle + y] for y in range(n2)]
    left = merge_sort(L)
    right = merge_sort(R)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result
#print(A)
B = merge_sort(A)
#print(B)
