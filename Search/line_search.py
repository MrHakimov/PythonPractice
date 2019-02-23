# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
def line_search(A, v):
    n = len(A)
    for j in range(n):
        if A[j] == v:
            return j
    return "NIL"
A = [1, 2, 3, 4, 5, 6]
v = 6
print(line_search(A, v))
