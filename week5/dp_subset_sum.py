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
    
    return table[T][len(X)]

