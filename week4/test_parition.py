import random
import logging
from week4.parition import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_partition():
    iter = 100
    for _ in range(iter):
        n = 100
        arr = [i for i in range(n)]
        random.shuffle(arr)
        pivot = arr[0]
        lo = 0
        hi = len(arr) - 1
        assert partition(arr, lo, hi) == pivot

def test_partition3_1():
    arr = [3,8,9,2,5,3,4,3,1,7,0,6]
    lo = 0
    hi = len(arr) - 1
    low, high = partition3(arr, lo, hi)
    assert low == 3 and high == 5

def test_partition3_2():
    iter = 100
    for _ in range(iter):
        n = 100
        arr = [i for i in range(n)]
        random.shuffle(arr)
        pivot = arr[0]
        
        repeat = 3
        for _ in range(repeat):
            arr.append(pivot)
        
        lo = 0
        hi = len(arr) - 1
        low, high = partition3(arr, lo, hi)
        LOGGER.debug(f'Pivot element : {pivot}')
        assert low == pivot and high == low + repeat