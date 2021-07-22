import random
import logging
from week5.dp_longest_common_subsequence import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_dp_longest_common_subsequence1():
    seq1 = [2,7,5]
    seq2 = [2,5]
    assert dp_longest_common_subsequence(seq1, seq2) == 2

def test_dp_longest_common_subsequence2():
    seq1 = "ABCDGH" 
    seq2 = "AEDFHR"
    assert dp_longest_common_subsequence(seq1, seq2) == 3

def test_dp_longest_common_subsequence3():
    seq1 = "abcd1e2"  
    seq2 = "bc12ea"  
    seq3 = "bd1ea"
    assert dp_longest_common_subsequence3(seq1, seq2, seq3) == 3