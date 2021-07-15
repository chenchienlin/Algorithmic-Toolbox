def dp_edit_distance(str1, str2):
    # If a string with length 0
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    # Init memoization data structure
    max_edit = len(str1) + len(str2)
    table = [[max_edit for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    
    # Compute recurence base case
    for row in range(len(str1)+1):
        table[row][0] = row
    for col in range(len(str2)+1):
        table[0][col] = col
    
    # Compute from i=1:len(str1) j=1:len(str2)
    for i in range(1, len(str1)+1): # i : row
        for j in range(1, len(str2)+1): # j : col
            match_and_mismatch = table[i-1][j-1]
            if str1[i-1] != str2[j-1]:
                match_and_mismatch += 1
            insertion = 1 + table[i-1][j]
            deletion = 1 + table[i][j-1]
            table[i][j] = min(match_and_mismatch, insertion, deletion)
    return table[len(str1)][len(str2)]