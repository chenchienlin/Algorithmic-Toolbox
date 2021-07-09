def longest_increasing_subsequence(seq, i, curr_max):
    if i == len(seq):
        return 0
    else:
        # include i
        a = None
        if seq[i] >= curr_max:
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
        if seq[i] >= curr_max:
            a = construct_longest_increasing_subsequence(seq, i+1, seq[i])
            a.insert(0,seq[i]) # append at first position
        
        # exclude i
        b = construct_longest_increasing_subsequence(seq, i+1, curr_max)
        
        if a is not None:
            return a if len(a) > len(b) else b
        else:
            return b

def longest_increasing_subsequence2(seq):
    best = 0
    for i in range(len(seq)):
        a = recur_increasing_subsequence(seq, i)
        if a > best:
                best = a
    return best

def recur_increasing_subsequence(seq, i):
    if i == len(seq):
        return 1
    else:
        best = 0
        for j in range(i+1, len(seq)):
            if seq[j] >= seq[i]:
                a = recur_increasing_subsequence(seq, j)
                if a > best:
                    best = a
        return best + 1