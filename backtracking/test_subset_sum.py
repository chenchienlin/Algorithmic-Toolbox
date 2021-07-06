import logging
from backtracking.subset_sum import subset_sum
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_subset_sum1():
    X = [1,2,3]
    used = [None for _ in range(len(X))]
    T = 4
    curr_sum = 0
    round = 0
    assert subset_sum(X, used, T, curr_sum, round) == True

def test_subset_sum2():
    X = [8,6,7,5,3,10,9]
    used = [None for _ in range(len(X))]
    T = 15
    curr_sum = 0
    round = 0
    assert subset_sum(X, used, T, curr_sum, round) == True

def test_subset_sum3():
    X = [11,6,5,1,7,13,12]
    used = [None for _ in range(len(X))]
    T = 15
    curr_sum = 0
    round = 0
    assert subset_sum(X, used, T, curr_sum, round) == False
