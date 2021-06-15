from week2.fibonacci_number import iter_fib
def fib_sum_partial_last_digit_naive(lo, hi):
    sum = 0
    for i in range(0, hi+1):
        if i >= lo and i <= hi:
            sum += iter_fib(i)
    return sum % 10


def iter_fib_sum_partial_last_digit(lo, hi):
    if hi < lo: return 'Error'
    if hi == 0:
        return 0
    if hi == 1:
        return 1
    else:
        a, b = 0, 1
        last_digit_sum = 0
        if lo <= 1:
            last_digit_sum += b
            last_digit_sum %= 10
        for i in range(2, hi+1):
            temp = b
            b = (a + b)%10
            a = temp%10
            if i >= lo and i <= hi:
                last_digit_sum += b
                last_digit_sum %= 10
        return last_digit_sum


import math
import numpy as np
def matrix_fib_sum_partial_last_digit(lo, hi):
    '''
        Assume matrix multiplication is O(1) and % operator is O(1), the time complexity is O(logn).
        Because there is only one digit in each entry of the matrix, there is no overhead for two 
        big numbers multiplication.
    '''
    if hi < lo: return 'Error'
    if hi <= 1: return hi
    
    m = math.floor(hi/2)
    M = np.matrix([[0, 1], [1, 1]])
    M2 = M ** 2
    V = np.matrix([[1, 0]]).T
    result = M * V
    last_digit_sum = 0
    if lo <= 1:
        last_digit_sum += result[0][0,0] % 10
        last_digit_sum += result[1][0,0] % 10
    for i in range(0, m): # i = 0,1,2,...,m-1
        M = M * M2
        
        # Store these for debugging
        M00 = M[0,0]
        M01 = M[0,1]
        M10 = M[1,0]
        M11 = M[1,1]
        
        M[0,0] = M[0,0] % 10
        M[0,1] = M[0,1] % 10
        M[1,0] = M[1,0] % 10
        M[1,1] = M[1,1] % 10
        
        result = M * V
        if lo <= 2*(i+1) and 2*(i+1) <= hi:
            last_digit_sum += result[0][0,0] % 10
        if lo <= 2*(i+1) + 1 and 2*(i+1) + 1 <= hi:
            last_digit_sum += result[1][0,0] % 10
        last_digit_sum %= 10
    return last_digit_sum