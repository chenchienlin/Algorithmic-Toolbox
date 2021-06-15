def iter_fib_sum_last_digit(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        
        sum = 0
        sum += b
        for i in range(2, n+1):
            temp = b
            b = (a + b)%10
            a = temp%10
            
            sum += b
        return sum

import math
import numpy as np
def matrix_fib_sum_last_digit(n):
    '''
        Assume matrix multiplication is O(1) and % operator is O(1), the time complexity is O(logn).
        Because there is only one digit in each entry of the matrix, there is no overhead for two 
        big numbers multiplication.
    '''
    if n <= 1: return n
    
    m = math.floor(n/2)
    M = np.matrix([[0, 1], [1, 1]])
    M2 = M ** 2
    V = np.matrix([[1, 0]]).T
    result = M * V
    last_digit_sum = 0
    last_digit_sum += result[0][0,0] % 10
    last_digit_sum += result[1][0,0] % 10
    for i in range(0, m):
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
        last_digit_sum += result[0][0,0] % 10
        last_digit_sum += result[1][0,0] % 10
    
    if n == 2*m:
        return last_digit_sum - result[1][0,0] % 10
    elif n == 2*m+1:
        return last_digit_sum