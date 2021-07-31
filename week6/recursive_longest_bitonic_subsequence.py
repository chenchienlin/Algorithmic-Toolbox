import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def longest_decreasing_subsequence(seq):
    seq_copy = seq.copy()
    seq_copy.insert(0, float('inf'))
    return recur_LDS(seq_copy, i=0, j=1)

def recur_LDS(seq, i, j):
    if j == len(seq):
        return 0
    elif seq[i] <= seq[j]:
        return recur_LDS(seq, i, j+1)
    else:
        # include j
        a = recur_LDS(seq, j, j+1) + 1
        
        # exclude j
        b = recur_LDS(seq, i, j+1)
        return max(a, b)

def recursive_longest_bitonic_subsequence(seq):
    seq_copy = seq.copy()
    seq_copy.insert(0, float('-inf'))
    return recur_LBS(seq_copy, i=0, j=1)

def recur_LBS(seq, i, j):
    if j == len(seq):
        return 0
    elif seq[i] >= seq[j]:
        # skip
        a = recur_LBS(seq, i, j+1)
        # find decreasing
        b = recur_LDS(seq, i, j)
        return max(a, b)
    else:
        # skip
        a = recur_LBS(seq, i, j+1)
        # find decreasing
        b = recur_LDS(seq, i, j)
        # take
        c = recur_LBS(seq, j, j+1) + 1
        return max(a, b, c)