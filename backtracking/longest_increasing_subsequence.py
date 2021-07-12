import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def longest_increasing_subsequence(seq, i, curr_max):
    if i == len(seq):
        return 0
    else:
        # include i
        a = None
        if seq[i] > curr_max:
            a = longest_increasing_subsequence(seq, i+1, seq[i]) + 1
        
        # exclude i
        b = longest_increasing_subsequence(seq, i+1, curr_max)
        
        return max(a,b) if a is not None else b

def construct_longest_increasing_subsequence(seq, i, curr_max):
    if i == len(seq):
        return []
    else:
        # include i
        a = None
        if seq[i] > curr_max:
            a = construct_longest_increasing_subsequence(seq, i+1, seq[i])
            a.insert(0,seq[i]) # append at first position
        
        # exclude i
        b = construct_longest_increasing_subsequence(seq, i+1, curr_max)
        
        if a is not None:
            return a if len(a) > len(b) else b
        else:
            return b

def longest_increasing_subsequence2(seq):
    seq_copy = seq.copy()
    seq_copy.insert(0, float('-inf'))
    return recur_LIS1(seq_copy, i=0, j=1)

def recur_LIS1(seq, i, j):
    if j == len(seq):
        return 0
    elif seq[i] > seq[j]:
        return recur_LIS1(seq, i, j+1)
    else:
        # include i
        a = recur_LIS1(seq, j, j+1) + 1
        
        # exclude j
        b = recur_LIS1(seq, i, j+1)
        if a > b:
            LOGGER.info(f'take {seq[j]}')
        else:
            LOGGER.info(f'skip {seq[j]}')
        return max(a, b)

def longest_increasing_subsequence3(seq):
    best = 0
    for i in range(len(seq)):
        a = recur_LIS2(seq, i)
        if a > best:
                best = a
    return best

def recur_LIS2(seq, i):
    if i == len(seq):
        return 1
    else:
        best = 0
        for j in range(i+1, len(seq)):
            if seq[j] > seq[i]:
                a = recur_LIS2(seq, j)
                if a > best:
                    best = a
        return best + 1