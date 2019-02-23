# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
def MERGE(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = A[:q] #[A[p + x - 1] for x in range(n1)]
    R = A[q:] #[A[q + y] for y in range(n2)]
    L.append(float('inf'))
    R.append(float('inf'))
    i=0
    j=0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
                        
def MERGE_SORT(A,p,r):
    if p < r:
        q = int((p+r)/2)
        MERGE_SORT(A,p,q)
        MERGE_SORT(A,q+1,r)
        MERGE(A,p,q,r)
    
        
    
A = [4, 3, 21, 7, 20, 1, 2, 5]
print(A)
MERGE_SORT(A, 0, len(A) - 1)
print(A)


