import math
def uniquePaths(m, n):
    return math.factorial((m-1) + (n-1)) / (math.factorial(m-1) * math.factorial(n-1))

assert uniquePaths(3, 7) == 28
assert uniquePaths(3, 2) == 3
assert uniquePaths(7, 3) == 28
assert uniquePaths(3, 3) == 6