import math
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def merge_n_inversions(arr, aux, lo, mid, hi):
    for k in range(lo, hi+1):
        aux[k] = arr[k]
    i = lo
    j = mid + 1
    n = 0
    for k in range(lo, hi+1):
        if i <= mid and j <= hi:
            if aux[i] <= aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                n += (mid-i+1)
                for ii in range(i, mid+1):
                    LOGGER.debug(f'Inversion pair : {aux[j]}, {aux[ii]}')
                j += 1
        else:
            if i > mid:
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1
    return n

def mergesort_n_inversions(arr):
    aux = arr.copy()
    lo = 0
    hi = len(arr) - 1
    return recur_mergesort(arr, aux, lo, hi)

def recur_mergesort(arr, aux, lo, hi):
    if hi > lo:
        mid = int(math.floor( (lo+hi)/2 ))
        n_inv1 = recur_mergesort(arr, aux, lo, mid)
        n_inv2 = recur_mergesort(arr, aux, mid+1, hi)
        n_inv3 = merge_n_inversions(arr, aux, lo, mid, hi)
        
        return n_inv1 + n_inv2 + n_inv3
    return 0