def dp_longest_bitonic_subsequence(seq):
    seq_copy = seq.copy()
    seq_copy.insert(0, float('inf'))
    n = len(seq_copy)
    lds = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    # Recursion base case
    for i in range(n+1):
        lds[i][n] = 0
    
    for j in reversed(range(1, n)):
        for i in range(0, j):
            assert i < j
            keep = 1 + lds[j][j+1]
            skip = lds[i][j+1]
            if seq_copy[i] <= seq_copy[j]:
                lds[i][j] = skip
            else:
                lds[i][j] = max(keep, skip)
    
    seq.insert(0, float('-inf'))
    lbs = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    # Recursion base case
    for i in range(n+1):
        lbs[i][n] = 0
    
    for j in reversed(range(1, n)):
        for i in range(0, j):
            assert i < j
            keep = 1 + lbs[j][j+1]
            skip = lbs[i][j+1]
            decs = lds[i][j]
            if seq[i] >= seq[j]:
                lbs[i][j] = max(skip, decs)
                # lbs[i][j] = skip
            else:
                lbs[i][j] = max(keep, skip, decs)
                # lbs[i][j] = max(keep, skip)
    return lbs[0][1]