def dp_wildcard_pattern_matching(string, pattern):
    # Init memoization data structure
    table = [[None for _ in range(len(pattern)+1)] for _ in range(len(string)+1)]
    
    # Recursion base case
    for i in range(len(string)+1):
        table[i][len(pattern)] = False
    for j in range(len(pattern)+1):
        table[len(string)][j] = False
    table[len(string)][len(pattern)] = True
    
    # Compute from i = len(string)-1:0 j = len(pattern)-1:0
    for i in reversed(range(len(string))):
        for j in reversed(range(len(pattern))):
            if string[i] == pattern[j] or pattern[j] == "?":
                table[i][j] = table[i+1][j+1]
            elif pattern[j] == "*":
                table[i][j] = table[i][j+1] or table[i+1][j+1] or table[i+1][j]
            else:
                table[i][j] = False
    return table[0][0]