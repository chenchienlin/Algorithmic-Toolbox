import math
def majority_element_voting(arr):
    n = len(arr)
    maj_idx = 0
    freq = 1
    
    for i in range(1, n):
        if arr[i] == arr[maj_idx]:
            freq -= 1
            if freq == 0:
                maj_idx = i
                freq = 1
        else:
            freq += 1
    
    freq = 0
    for i in range(0, n):
        if arr[i] == arr[maj_idx]:
            freq += 1
    
    if freq > int(math.floor(n/2)):
        return arr[maj_idx]
    else:
        return None