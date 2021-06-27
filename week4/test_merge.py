import random
import logging
from week4.merge import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

import math
def test_merge1():
    arr = [5,6,7,8,1,2,3,4]
    aux = arr.copy()
    lo = 0
    hi = len(arr) - 1
    mid = int(math.floor( (lo + hi)/2 ))
    merge(arr, aux, lo, mid, hi)
    assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) == True

def test_merge2():
    lo_range = 0
    hi_range = 100
    n = 10
    iter = 100
    for _ in range(iter):
        arr1 = sorted([random.randint(lo_range, hi_range) for _ in range(n)])
        arr2 = sorted([random.randint(lo_range, hi_range) for _ in range(n)])
        assert all(arr1[i] <= arr1[i+1] for i in range(len(arr1)-1)) == True
        assert all(arr2[i] <= arr2[i+1] for i in range(len(arr2)-1)) == True
        LOGGER.debug(arr1)
        LOGGER.debug(arr2)
        
        arr = arr1.copy()
        arr.extend(arr2)
        aux = arr.copy()
        LOGGER.debug(arr)
        lo = 0
        hi = len(arr) - 1
        mid = int(math.floor( (lo + hi)/2 ))
        merge(arr, aux, lo, mid, hi)
        assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) == True
        LOGGER.debug(arr)