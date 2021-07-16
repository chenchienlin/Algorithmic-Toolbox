import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def dp_subset_sum(X, T):
    # Init memoization data structure
    table = [[False for _ in range(len(X)+1)] for _ in range(T+1)]
    
    # Recursion base case
    for col in range(len(X)+1):
        table[0][col] = True
    
    # Compute from t=1:T j=1:len(X)
    for t in range(1, T+1):
        for i in range(1, len(X)+1):
            idx = i-1
            val = X[idx]
            b = table[t][i-1]
            if val <= t:
                newb = table[t-val][i-1]
                if newb == True:
                    b = True
            table[t][i] = b
    for r in table:
        LOGGER.debug(r)
    l = construct_subset_sum(T, X, table)
    return table[T][len(X)], l

def construct_subset_sum(T, X, table):
    i = len(X)
    l = []
    while T > 0 and i > 0:
        idx = i - 1
        if table[T-X[idx]][i-1] and T - X[idx] >= 0:
            i -= 1
            T -= X[idx]
            l.append(X[idx])
        else:
            i -= 1
    return l