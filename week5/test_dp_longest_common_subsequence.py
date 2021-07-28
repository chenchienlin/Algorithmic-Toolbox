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

def test_dp_longest_common_subsequence3_1():
    seq1 = "abcd1e2"  
    seq2 = "bc12ea"  
    seq3 = "bd1ea"
    assert dp_longest_common_subsequence3(seq1, seq2, seq3) == 3

def test_dp_longest_common_subsequence3_2():
    seq1 = "AGGT12"
    seq2 = "12TXAYB"
    seq3 = "12XBA"
    assert dp_longest_common_subsequence3(seq1, seq2, seq3) == 2

def test_construct_all_longest_common_subsequence1():
    seq1 = "ABCBDAB"
    seq2 = "BDCABA"
    assert dp_longest_common_subsequence(seq1, seq2) == 4
    results = construct_all_longest_common_subsequence(seq1, seq2)
    ans = ['BCBA','BDAB','BCAB']
    for res in results:
        assert len(res) == 4
        assert res in ans

def test_construct_all_longest_common_subsequence2():
    seq1 = "abcabcaa"
    seq2 = "acbacba"
    results = construct_all_longest_common_subsequence(seq1, seq2)
    ans = ['ababa','abaca','abcba','acaba','acaca','acbaa','acbca']
    S = set()
    for res in results:
        LOGGER.debug(res)
        assert res not in S
        S.add(res)
        ans.remove(res)
    assert len(ans) == 0