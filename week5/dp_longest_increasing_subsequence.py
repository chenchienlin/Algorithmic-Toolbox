def dp_longest_increasing_subsequence(seq):
    seq = seq.copy()
    seq.insert(0, float('-inf'))
    n = len(seq)
    table = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        table[i][n] = 0
    for j in reversed(range(1, n)):
        for i in range(0, j):
            assert i < j
            keep = 1 + table[j][j+1]
            skip = table[i][j+1]
            if seq[i] >= seq[j]:
                table[i][j] = skip
            else:
                table[i][j] = max(keep, skip)