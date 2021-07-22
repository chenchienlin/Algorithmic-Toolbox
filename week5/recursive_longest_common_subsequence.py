def recursive_longest_common_subsequence(seq1, seq2, i, j):
    if i == len(seq1):
        return 0
    if j == len(seq2):
        return 0
    if seq1[i] == seq2[j]:
        return 1 + recursive_longest_common_subsequence(seq1, seq2, i+1, j+1)
    else:
        a = recursive_longest_common_subsequence(seq1, seq2, i+1, j)
        b = recursive_longest_common_subsequence(seq1, seq2, i, j+1)
        return max(a, b)

def recursive_longest_common_subsequence2(seq1, seq2, leni, lenj):
    if leni == 0:
        return 0
    if lenj == 0:
        return 0
    if seq1[leni-1] == seq2[lenj-1]:
        return 1 + recursive_longest_common_subsequence2(seq1, seq2, leni-1, lenj-1)
    else:
        a = recursive_longest_common_subsequence2(seq1, seq2, leni-1, lenj)
        b = recursive_longest_common_subsequence2(seq1, seq2, leni, lenj-1)
        return max(a, b)

def recursive_longest_common_subsequence3(seq1, seq2, seq3, leni, lenj, lenk):
    ''' Computes the length of a longest common subsequence of three sequences.
    '''
    if leni == 0 or lenj == 0 or lenk == 0:
        return 0
    elif seq1[leni-1] == seq2[lenj-1] == seq3[lenk-1]:
        return 1 + recursive_longest_common_subsequence3(seq1, seq2, seq3, leni-1, lenj-1, lenk-1)
    else:
        a = recursive_longest_common_subsequence3(seq1, seq2, seq3, leni-1, lenj, lenk)
        b = recursive_longest_common_subsequence3(seq1, seq2, seq3, leni, lenj-1, lenk)
        c = recursive_longest_common_subsequence3(seq1, seq2, seq3, leni, lenj, lenk-1)
        return max(a, b, c)