# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
def line_find_max_subarray(A):
    max_sum = 0
    start_index = 0
    end_index = 0
    sums = 0
    n = len(A)
    for i in range(n):
        if sums == 0:
            start_index = i
        sums += A[i]
        if max_sum < sums:
            max_sum = sums
            end_index = i
        if sums < 0:
            sums = 0

    return (start_index, end_index, max_sum)

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(line_find_max_subarray(A))