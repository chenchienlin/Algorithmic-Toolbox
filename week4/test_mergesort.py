import random
import logging
from week4.mergesort import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_mergesort1():
    arr = [5,6,7,8,1,2,3,4]
    mergesort(arr)
    LOGGER.debug(arr)
    assert arr == sorted(arr)

def test_mergesort2():
    lo_range = 0
    hi_range = 100
    n = 100
    iter = 100
    for _ in range(iter):
        arr = sorted([random.randint(lo_range, hi_range) for _ in range(n)]) 
        mergesort(arr)
        LOGGER.debug(arr)
        assert arr == sorted(arr)

def test_mergesort3():
    lo_range = -100
    hi_range = 100
    n = 200
    iter = 100
    for _ in range(iter):
        arr = sorted([random.randint(lo_range, hi_range) for _ in range(n)])
        mergesort(arr)
        LOGGER.debug(arr)
        assert arr == sorted(arr)