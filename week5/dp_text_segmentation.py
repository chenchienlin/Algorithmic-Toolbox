import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def is_word(string, dictionary):
    return string in dictionary

def memo_splitable(S, i, dictionary, memo):
    if i == len(S):
        return True
    for j in range(i, len(S)):
        substr = S[i:j+1]
        if is_word(substr, dictionary):
            LOGGER.debug(f'{substr} {is_word(substr, dictionary)}')
            if j+1 in memo and memo[j+1] is True:
                return True
            else:
                memo[j+1] = memo_splitable(S, j+1, dictionary, memo)
                if memo[j+1] is True:
                    return True
    return False

def dp_splitable(S, dictionary):
    # Init memoization data structure
    table = [None for _ in range(len(S)+1)]
    
    # Compute recurrence base case
    table[len(S)] = True
    
    # Compute from i=len(S)-1:0 j=i:len(S)-1
    j = len(S) - 1
    for i in reversed(range(len(S))):
        for j in range(i, len(S)):
            substr = S[i:j+1]
            if is_word(substr, dictionary) and table[j+1]:
                table[i] = True
                break
            table[i] = False
    return table[0]

def dp_splitable2(S, dictionary):
    # Init memoization data structure
    table = [None for _ in range(len(S)+1)]
    
    # Compute recurrence base case
    table[len(S)] = True
    
    # Compute from i=len(S)-1:0 j=i:len(S)-1
    j = len(S) - 1
    for i in reversed(range(len(S))):
        for j in range(i, len(S)):
            substr = S[i:j+1]
            if is_word(substr, dictionary) and table[j+1]:
                table[i] = True
                break
            table[i] = False
    return construct_all_segmentations(S, dictionary, table, i=0)

def construct_all_segmentations(S, dictionary, table, i):
    if i == len(S):
        return ""
    results = []
    for j in range(i, len(S)):
        substr = S[i:j+1]
        if is_word(substr, dictionary) and table[j+1]:
            res = construct_all_segmentations(S, dictionary, table, j+1)
            if res == "":
                res = substr
                results.append(res)
            elif isinstance(res, list):
                for seg in res:
                    seg = f"{substr} {seg}"
                    results.append(seg)
    return results