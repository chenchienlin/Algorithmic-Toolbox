import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def dp_longest_common_subsequence(seq1, seq2):
    if len(seq1) == 0:
        return 0
    if len(seq2) == 0:
        return 0
    # Init memoization data structure
    table = [[-1 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    
    # Compute recurrence base case
    for row in range(len(seq1)+1):
        table[row][0] = 0
    for col in range(len(seq2)+1):
        table[0][col] = 0
    
    # Compute from i=1:len(seq1) j=1:len(seq2)
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            if seq1[i-1] == seq2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[len(seq1)][len(seq2)]

def dp_longest_common_subsequence3(seq1, seq2, seq3):
    ''' Computes the length of a longest common subsequence of three sequences.
    '''
    table = [[[-1 for _ in range(len(seq3)+1)] for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    
    # Compute recurrence base case
    for k in range(len(seq3)+1):
        for j in range(len(seq2)+1):
            table[0][j][k] = 0
    
    for k in range(len(seq3)+1):
        for i in range(len(seq1)+1):
            table[i][0][k] = 0
    
    for j in range(len(seq2)+1):
        for i in range(len(seq1)+1):
            table[i][j][0]
    
    # Compute from i=1:len(seq1) j=1:len(seq2)  k=1:len(seq3)
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            for k in range(1, len(seq3)+1):
                if seq1[i-1] == seq2[j-1] == seq3[k-1]:
                    table[i][j][k] = 1 + table[i-1][j-1][k-1]
                else:
                    table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k], table[i][j][k-1])
    return table[len(seq1)][len(seq2)][len(seq3)]

def construct_longest_common_subsequence(seq1, seq2):
    if len(seq1) == 0:
        return 0
    if len(seq2) == 0:
        return 0
    # Init memoization data structure
    table = [[-1 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    
    # Compute recurrence base case
    for row in range(len(seq1)+1):
        table[row][0] = 0
    for col in range(len(seq2)+1):
        table[0][col] = 0
    
    # Compute from i=1:len(seq1) j=1:len(seq2)
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            if seq1[i-1] == seq2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return construct_sequence(seq1, seq2, table)

def construct_all_longest_common_subsequence(seq1, seq2):
    if len(seq1) == 0:
        return 0
    if len(seq2) == 0:
        return 0
    # Init memoization data structure
    table = [[-1 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    
    # Compute recurrence base case
    for row in range(len(seq1)+1):
        table[row][0] = 0
    for col in range(len(seq2)+1):
        table[0][col] = 0
    
    # Compute from i=1:len(seq1) j=1:len(seq2)
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            if seq1[i-1] == seq2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return construct_all_sequences(seq1, seq2, table, len(seq1), len(seq2))

def construct_sequence(seq1, seq2, table):
    i = len(seq1)
    j = len(seq2)
    result = []
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            i -= 1
            j -= 1
            result.insert(0, seq1[i])
        elif table[i-1][j] == table[i][j]:
            i -= 1
            continue
        else:
            j -= 1
    return result

def construct_all_sequences(seq1, seq2, table, i, j):
    if i == 0 and j == 0:
        return [""]
    elif seq1[i-1] == seq2[j-1] and i-1 >= 0 and j-1 >= 0:
        res = construct_all_sequences(seq1, seq2, table, i-1, j-1)
        for k in range(len(res)):
            res[k] = f'{res[k]}{seq1[i-1]}'
        return res
    else:
        res1, res2 = [], []
        if table[i-1][j] == table[i][j] and i-1 >= 0:
            res1 = construct_all_sequences(seq1, seq2, table, i-1, j)
        if table[i][j-1] == table[i][j] and j-1 >= 0:
            res2 = construct_all_sequences(seq1, seq2, table, i, j-1)
        if len(res1) == 0:
            return [*res2]
        elif len(res2) == 0:
            return [*res1]
        res = res1 + list(set(res2) - set(res1)) # combine two lists without duplicates
        return res