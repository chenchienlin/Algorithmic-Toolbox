import logging
from week6.dp_longest_bitonic_subsequence import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_longest_bitonic_subsequence1():
    seq = [4,2,5,9,7,6,10,3,1]
    assert dp_longest_bitonic_subsequence(seq) == 7

def test_recursive_longest_bitonic_subsequence2():
    seq = [1, 11, 2, 10, 4, 5, 2, 1]
    assert dp_longest_bitonic_subsequence(seq) == 6

def test_recursive_longest_bitonic_subsequence3():
    seq = [12, 11, 40, 5, 3, 1]
    assert dp_longest_bitonic_subsequence(seq) == 5

def test_recursive_longest_bitonic_subsequence4():
    seq = [80, 60, 30, 40, 20, 10]
    assert dp_longest_bitonic_subsequence(seq) == 5