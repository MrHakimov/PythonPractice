# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
def hard_find_max_subarray(A):
    max_sum = 0
    start = 0
    end  = 0
    n = len(A)
    for i in range(n):
        summ = 0
        for j in range(n-i):
            summ += A[j+i]
            if max_sum < summ:
                max_sum = summ
                start = i
                end = j+i
    return (start, end, max_sum)

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(hard_find_max_subarray(A))
