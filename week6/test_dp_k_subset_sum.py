import time
import logging
from week6.recursive_k_subset_sum import recursive_k_subset_sum
from week6.dp_k_subset_sum import dp_k_subset_sum
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_k_subset_sum1():
    X = [2, 1, 4, 5, 6]
    K = 2
    assert recursive_k_subset_sum(X, K) == True
    K = 3
    assert recursive_k_subset_sum(X, K) == True
    K = 6
    assert recursive_k_subset_sum(X, K) == False

def test_recursive_k_subset_sum2():
    X = [4,3,2,3,5,2,1]
    K = 2
    assert recursive_k_subset_sum(X, K) == True
    K = 4
    assert recursive_k_subset_sum(X, K) == True
    K = 5
    assert recursive_k_subset_sum(X, K) == False

def test_recursive_k_subset_sum3():
    X = [17,59,34,57,17,23,67,1,18,2,59]
    K = 3
    begin = time.time()
    assert recursive_k_subset_sum(X, K) == True
    end = time.time()
    LOGGER.info(f'Backtracking {end-begin} s')
    
    begin = time.time()
    assert dp_k_subset_sum(X, K) == True
    end = time.time()
    LOGGER.info(f'DP {end-begin} s')