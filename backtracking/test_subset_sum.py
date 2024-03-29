import logging
from backtracking.subset_sum import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_subset_sum1():
    X = [1,2,3]
    used = [None for _ in range(len(X))]
    T = 4
    curr_sum = 0
    round = 0
    assert subset_sum(X, used, T, curr_sum, round) == True
    
    i = len(X)-1
    assert subset_sum_clean(X, i, T) == True

def test_subset_sum2():
    X = [8,6,7,5,3,10,9]
    used = [None for _ in range(len(X))]
    T = 15
    curr_sum = 0
    round = 0
    assert subset_sum(X, used, T, curr_sum, round) == True
    
    i = len(X)-1
    assert subset_sum_clean(X, i, T) == True

def test_subset_sum3():
    X = [11,6,5,1,7,13,12]
    used = [None for _ in range(len(X))]
    T = 15
    curr_sum = 0
    round = 0
    assert subset_sum(X, used, T, curr_sum, round) == False
    
    i = len(X)-1
    assert subset_sum_clean(X, i, T) == False

def test_construct_subset_sum1():
    X = [1,2,3]
    i = len(X)-1
    T = 4
    result = construct_subset_sum(X, i, T)
    LOGGER.debug(result)
    assert sum(result) == T

def test_construct_subset_sum2():
    X = [8,6,7,5,3,10,9]
    i = len(X)-1
    T = 15
    result = construct_subset_sum(X, i, T)
    LOGGER.debug(result)
    assert sum(result) == T

def test_construct_subset_sum3():
    X = [11,6,5,1,7,13,12]
    i = len(X)-1
    T = 15
    result = construct_subset_sum(X, i, T)
    LOGGER.debug(result)
    assert result == None