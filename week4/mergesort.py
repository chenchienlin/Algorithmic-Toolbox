import math
import logging
from week4.merge import merge
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def mergesort(arr):
    aux = arr.copy()
    lo = 0
    hi = len(arr) - 1
    recur_mergesort(arr, aux, lo, hi)

def recur_mergesort(arr, aux, lo, hi):
    if hi > lo:
        mid = int(math.floor( (lo+hi)/2 ))
        recur_mergesort(arr, aux, lo, mid)
        recur_mergesort(arr, aux, mid+1, hi)
        merge(arr, aux, lo, mid, hi)