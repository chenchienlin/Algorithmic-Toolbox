def place_min(S, min_val, min_len):
    if len(S) > min_len:
        elem = S.pop(0)
        if elem < min_val:
            min_val = elem
        replaced, min_val = place_min(S, min_val, min_len)
        if elem == min_val and replaced is False:
            return True, min_val
        else:
            S.insert(0, elem)
            return replaced, min_val
    else:
        S.insert(0, min_val)
        return False, min_val

def stack_sort(S, min_len):
    if min_len < len(S):
        place_min(S, float('inf'), min_len)
        stack_sort(S, min_len+1)

S = [-1,-2,-1,-2,-1,-2]
stack_sort(S, 0)
print(S)