def dp_longest_palindromic_substring(s):
    # Init memoization data structure
    table = [[None for _ in range(len(s))] for _ in range(len(s))]
    besti = bestj = 0
    
    # Compute recurrence base case
    for i in range(len(s)):
        # Base case 1: a char itself is a palindrome
        table[i][i] = True
        
        # Base case 2: substring(i, i+1) is a palindrome
        # if s[i] == s[j] (length 2 palindrome)
        if i+1 < len(s):            
            if s[i] == s[i+1]:
                table[i][i+1] = True
                besti, bestj = i, i+1
            else:
                table[i][i+1] = False
    
    # Compute from i=len(s):0 j=len(s):i+2
    for i in reversed(range(len(s))):
        for j in reversed(range(i+2, len(s))):
            if s[i] == s[j] and table[i+1][j-1]:
                table[i][j] = True
                if j - i > bestj - besti:
                    besti, bestj = i, j
            else:
                table[i][j] = False
    return s[besti:bestj+1]

def dp_longest_palindromic_substring2(s):
    besti = bestj = 0
    
    for i in range(len(s)):
        j = i+1
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            if j - i > bestj - besti:
                    besti, bestj = i, j
            i, j = i-1, j+1
    
    for i in range(len(s)):
        j = i+2
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            if j - i > bestj - besti:
                    besti, bestj = i, j
            i, j = i-1, j+1
    return s[besti:bestj+1]