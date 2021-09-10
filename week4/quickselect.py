from week4.parition import partition
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def quickselect(arr, k):
    lo = 0
    hi = len(arr) - 1
    if k < lo or k > hi: return -1
    while hi >= lo:
        p = partition(arr, lo, hi)
        if k == p:
            return arr[p]
        if k < p:
            hi = p - 1
        else:
            lo = p + 1

def recur_quickselect(arr, lo, hi, k):
    p = partition(arr, lo, hi)
    
    if k == p:
        return arr[p]
    elif k < p:
        return recur_quickselect(arr, lo, p-1, k)
    else:
        return recur_quickselect(arr, p+1, hi, k)

def find_kth_largest(nums, k):
    k = len(nums) - k
    return quickselect(nums, k)

def recur_find_kth_largest(nums, k):
    k = len(nums) - k
    lo, hi = 0, len(nums) - 1
    return recur_quickselect(nums, lo, hi, k)