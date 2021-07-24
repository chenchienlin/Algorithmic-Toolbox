import random
import logging
from week5.recursive_longest_common_subsequence import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_longest_common_subsequence1():
    seq1 = [2,7,5]
    seq2 = [2,5]
    assert recursive_longest_common_subsequence(seq1, seq2, i=0, j=0) == 2
    assert recursive_longest_common_subsequence2(seq1, seq2, len(seq1), len(seq2)) == 2

def test_recursive_longest_common_subsequence2():
    seq1 = "ABCDGH" 
    seq2 = "AEDFHR"
    assert recursive_longest_common_subsequence(seq1, seq2, i=0, j=0) == 3
    assert recursive_longest_common_subsequence2(seq1, seq2, len(seq1), len(seq2)) == 3

def test_recursive_longest_common_subsequence3_1():
    seq1 = "abcd1e2"  
    seq2 = "bc12ea"  
    seq3 = "bd1ea"
    assert recursive_longest_common_subsequence3(seq1, seq2, seq3, len(seq1), len(seq2), len(seq3)) == 3

def test_recursive_longest_common_subsequence3_2():
    seq1 = "AGGT12"
    seq2 = "12TXAYB"
    seq3 = "12XBA"
    assert recursive_longest_common_subsequence3(seq1, seq2, seq3, len(seq1), len(seq2), len(seq3)) == 2