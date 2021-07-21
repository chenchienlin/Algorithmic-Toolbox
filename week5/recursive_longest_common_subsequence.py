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