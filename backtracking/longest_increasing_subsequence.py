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