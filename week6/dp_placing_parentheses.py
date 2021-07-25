# from week6.recursive_placing_parentheses import compute
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def compute(ops, i, a, b):
    if ops[i] == '+':
        return a + b
    elif ops[i] == '-':
        return a - b
    elif ops[i] == '*':
        return a * b
    elif ops[i] == '/':
        return a / b

def dp_placing_parentheses(nums, ops):
    # Init memoization data structure
    M = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    m = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    
    # Compute recurrence base case
    for i in range(len(nums)):
        M[i][i] = nums[i]
        m[i][i] = nums[i]
    
    for s in range(1, len(nums)):
        for i in range(0, len(nums)-s):
            j = i + s
            best_min = float('inf')
            best_max = float('-inf')
            LOGGER.debug(f'entry : {i}, {j}')
            for k in range(i, j):
                a = compute(ops, k, M[i][k], M[k+1][j])
                b = compute(ops, k, M[i][k], m[k+1][j])
                c = compute(ops, k, m[i][k], M[k+1][j])
                d = compute(ops, k, m[i][k], m[k+1][j])
                curr_min = min(a, b, c, d)
                curr_max = max(a, b, c, d)
                if curr_min < best_min:
                    best_min = curr_min
                if curr_max > best_max:
                    best_max = curr_max
            m[i][j] = best_min
            M[i][j] = best_max