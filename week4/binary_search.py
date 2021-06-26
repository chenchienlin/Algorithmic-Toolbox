def binary_search(l, target):
    sorted_list = sorted(l)
    lo = 0
    hi = len(l) - 1
    return recur_binary_search(sorted_list, lo, hi, target)

import math
def recur_binary_search(l, lo, hi, target):
    mid = int(math.floor(lo + hi)/2)
    if l[mid] == target:
        return mid
    if lo >= hi and l[mid] != target:
        return -1
    
    if l[mid] <= target:
        return recur_binary_search(l, mid+1, hi, target)
    else:
        return recur_binary_search(l, lo, mid-1, target)

def iter_binary_search(l, target):
    l = sorted(l)
    lo = 0
    hi = len(l) - 1
    
    while lo <= hi:
        mid = int(math.floor(lo + hi)/2)
        
        if l[mid] == target: 
            return mid
        elif l[mid] < target:
            lo = mid + 1
        elif l[mid] > target:
            hi = mid - 1
    return -1