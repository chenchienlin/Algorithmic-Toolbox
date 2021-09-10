import random
import logging
from week4.quickselect import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_quickselect1():
    arr = [4,3,1,7,2,6,5,8,0]
    sorted_arr = sorted(arr.copy(), reverse=True)
    lo = 0
    hi = len(arr)-1
    for k in range(1, len(arr)+1):
        a = find_kth_largest(arr.copy(), k)
        b =  recur_find_kth_largest(arr.copy(), k)
        LOGGER.debug(f'find_kth_largest  {k}_th largest : {a}')
        LOGGER.debug(f'recur_find_kth_largest  {k}_th largest : {b}')
        assert a == b == sorted_arr[k-1]

def test_quickselect2():
    iter = 100
    for _ in range(iter):
        arr = [i for i in range(-100, 100)]
        random.shuffle(arr)
        sorted_arr = sorted(arr.copy(), reverse=True)
        lo = 0
        hi = len(arr)-1
        for k in range(1, len(arr)+1):
            a = find_kth_largest(arr.copy(), k)
            b =  recur_find_kth_largest(arr.copy(), k)
            LOGGER.debug(f'find_kth_largest  {k}_th largest : {a}')
            LOGGER.debug(f'recur_find_kth_largest  {k}_th largest : {b}')
            assert a == b == sorted_arr[k-1]