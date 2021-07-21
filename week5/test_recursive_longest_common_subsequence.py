import random
import logging
from week5.recursive_longest_common_subsequence import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_longest_common_subsequence1():
    seq1 = [2,7,5]
    seq2 = [2,5]
    assert recursive_longest_common_subsequence(seq1, seq2, i=0, j=0) == 2

def test_recursive_longest_common_subsequence2():
    seq1 = "ABCDGH" 
    seq2 = "AEDFHR"
    assert recursive_longest_common_subsequence(seq1, seq2, i=0, j=0) == 3