import math

def recursive_longest_palindromic_subsequence(seq, i, ans):
    if i == len(seq):
        if len(ans) == 0:
            return 0
        mid = math.floor(len(ans)/2)
        if len(ans) % 2 == 0:
            rg = mid + 1
        else:
            rg = mid
        for j in range(rg):
            if ans[j] == ans[-j-1]:
                continue
            else:
                return 0
        return len(ans)
    a, b = 0, 0
    ans.append(seq[i])
    a = recursive_longest_palindromic_subsequence(seq, i+1, ans)
    ans.pop()
    b = recursive_longest_palindromic_subsequence(seq, i+1, ans)
    return max(a, b)