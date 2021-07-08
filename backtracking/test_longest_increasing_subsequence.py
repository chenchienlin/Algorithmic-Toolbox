import logging
from backtracking.longest_increasing_subsequence import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_longest_increasing_subsequence1():
    seq = [3,10,2,1,20]
    i = 0
    curr_max = float('-inf')
    longest_increasing_subsequence(seq, i, curr_max) == 3

def test_longest_increasing_subsequence2():
    seq = [3,2]
    i = 0
    curr_max = float('-inf')
    longest_increasing_subsequence(seq, i, curr_max) == 1

def test_longest_increasing_subsequence3():
    seq = [50,3,10,7,40,80]
    i = 0
    curr_max = float('-inf')
    longest_increasing_subsequence(seq, i, curr_max) == 4

def test_construct_longest_increasing_subsequence1():
    seq = [3,10,2,1,20]
    i = 0
    curr_max = float('-inf')
    assert construct_longest_increasing_subsequence(seq, i, curr_max) == [3,10,20]

def test_construct_longest_increasing_subsequence2():
    seq = [50,3,10,7,40,80]
    i = 0
    curr_max = float('-inf')
    assert construct_longest_increasing_subsequence(seq, i, curr_max) == [3,7,40,80]
