import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def recursive_longest_bitonic_subsequence(seq):
    seq_copy = seq.copy()
    seq_copy.insert(0, float('-inf'))
    best = 0
    for k in range(1, len(seq_copy)):
        a = recur_LIS(seq_copy, 0, 1, k+1) + recur_LDS(seq_copy, k, k+1, len(seq_copy))
        best = max(a, best)
    return best

def recur_LIS(seq, i, j, k):
    if j == k:
        return 0
    elif seq[i] >= seq[j]:
        return recur_LIS(seq, i, j+1, k)
    else:
        # include j
        a = recur_LIS(seq, j, j+1, k) + 1
        
        # exclude j
        b = recur_LIS(seq, i, j+1, k)
        return max(a, b)

def recur_LDS(seq, i, j, k):
    if j == k:
        return 0
    elif seq[i] <= seq[j]:
        return recur_LDS(seq, i, j+1, k)
    else:
        # include j
        a = recur_LDS(seq, j, j+1, k) + 1
        
        # exclude j
        b = recur_LDS(seq, i, j+1, k)
        return max(a, b)