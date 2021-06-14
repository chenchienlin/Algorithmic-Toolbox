def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)
    
def iter_fib(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            temp = b
            b = a + b
            a = temp
        return b

def mem_fib(n):
    memo = dict()
    return mem_fib_helper(n, memo)

def mem_fib_helper(n, memo):
    if n <= 1:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = mem_fib_helper(n-1, memo) + mem_fib_helper(n-2, memo)
            return memo[n]

import math
import numpy as np
def matrix_fib(n):
    '''
        Assume matrix multiplication is O(1), the time complexity is O(logn).
        When n is large, then the time complexity would be between O(logn) and O(n)
    '''
    m = math.floor(n/2)
    M = np.matrix([[0, 1], [1, 1]])
    M2 = M ** 2
    V = np.matrix([[1, 0]]).T
    for i in range(0, m):
        M = M * M2
    result = M * V
    if n == 2*m:
        return result[0][0,0]
    elif n == 2*m+1:
        return result[1][0,0]

def matrix_fib2(n):
    '''
        Time Complexity Depends on the effiency of M ** n
    '''
    M = np.matrix([[0, 1], [1, 1]])
    V = np.matrix([[1, 0]]).T
    M = M ** n
    result = M * V
    return result[1][0,0]