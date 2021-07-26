import logging
from week6.dp_partitioning_souvenirs import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_dp_partitioning_souvenirs1():
    X = [3,3,3,3]
    i = len(X)-1
    T = int(sum(X)/3)
    memo = dict()
    assert dp_partitioning_souvenirs(X, i, T, T, T, memo) == False

def test_dp_partitioning_souvenirs2():
    X = [17,59,34,57,17,23,67,1,18,2,59]
    i = len(X)-1
    T = int(sum(X)/3)
    memo = dict()
    assert dp_partitioning_souvenirs(X, i, T, T, T, memo) == True

def test_dp_partitioning_souvenirs3():
    X = [1,2,3,4,5,5,7,7,8,10,12,19,25]
    i = len(X)-1
    T = int(sum(X)/3)
    memo = dict()
    assert dp_partitioning_souvenirs(X, i, T, T, T, memo) == True

def test_dp_partitioning_souvenirs4():
    X = [7,3,2,1,5,4,8]
    i = len(X)-1
    T = int(sum(X)/3)
    memo = dict()
    assert dp_partitioning_souvenirs(X, i, T, T, T, memo) == True