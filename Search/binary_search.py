# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
def binary_search(A, v,i):
    print(A)
    a = "NIL"+str(i)
    i = i + 1
    n = len(A)-1
    q = int(n/2)
    print("q",q)
    if A[q] == v:
        print("Aq",A[q])
        a = "YES"
        print("a",a)
        return a
        print("="*10)
    else:
        if A[q] < v:
            A = A[q:n]
        else:
            A = A[0:q]
        binary_search(A,v,i)
        
    return a
A = [1, 2, 3, 4, 5, 6]
v = 6
print(binary_search(A, v,1))
