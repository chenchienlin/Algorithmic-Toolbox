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