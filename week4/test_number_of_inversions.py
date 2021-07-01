import math
import random
import logging
from week4.number_of_inversions import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_mergesort_n_inversions1():
    arr = [2,3,9,2,9]
    assert mergesort_n_inversions(arr) == 2

def test_mergesort_n_inversions2():
    arr = [8,4,2,1]
    assert mergesort_n_inversions(arr) == 6

def test_mergesort_n_inversions3():
    arr = [3,1,2]
    assert mergesort_n_inversions(arr) == 2