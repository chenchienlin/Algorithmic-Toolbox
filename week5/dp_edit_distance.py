import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def dp_edit_distance(str1, str2):
    # If a string with length 0
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    # Init memoization data structure
    max_edit = len(str1) + len(str2)
    table = [[max_edit for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    
    # Compute recurrence base case
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
    
    for r in table:
        LOGGER.debug(r)
    
    l1, l2 = construct_alignment(str1, str2, table)
    LOGGER.debug(l1)
    LOGGER.debug(l2)
    return table[len(str1)][len(str2)]

def construct_alignment(str1, str2, table):
    i = len(str1)
    j = len(str2)
    l1, l2 = [], []
    while i > 0 or j > 0:
        if i > 0 and table[i][j] == table[i-1][j] + 1:
            l1.insert(0, str1[i-1])
            l2.insert(0,'-')
            i -= 1
        elif j > 0 and table[i][j] == table[i][j-1] + 1:
            l1.insert(0, '-')
            l2.insert(0, str2[j-1])
            j -= 1
        else:
            l1.insert(0,str1[i-1])
            l2.insert(0,str2[j-1])
            i -= 1
            j -= 1
    return l1, l2