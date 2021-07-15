import logging
from week5.dp_subset_sum import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_subset_sum1():
    X = [1,2,3]
    T = 4
    assert dp_subset_sum(X, T) == True

def test_subset_sum2():
    X = [8,6,7,5,3,10,9]
    T = 15
    assert dp_subset_sum(X, T) == True

def test_subset_sum3():
    X = [11,6,5,1,7,13,12]
    T = 15
    assert dp_subset_sum(X, T) == False