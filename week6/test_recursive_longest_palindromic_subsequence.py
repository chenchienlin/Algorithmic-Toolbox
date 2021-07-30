import logging
from week6.recursive_longest_palindromic_subsequence import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_longest_palindromic_subsequence1():
    seq = 'ABBDCACB'
    i = 0
    ans = []
    assert recursive_longest_palindromic_subsequence(seq, i, ans) == 5
    j = len(seq) - 1
    assert recursive_longest_palindromic_subsequence2(seq, i, j) == 5

def test_recursive_longest_palindromic_subsequence2():
    seq = 'bbbab'
    i = 0
    ans = []
    assert recursive_longest_palindromic_subsequence(seq, i, ans) == 4
    j = len(seq) - 1
    assert recursive_longest_palindromic_subsequence2(seq, i, j) == 4

def test_recursive_longest_palindromic_subsequence3():
    seq = 'cbbd'
    i = 0
    ans = []
    assert recursive_longest_palindromic_subsequence(seq, i, ans) == 2
    j = len(seq) - 1
    assert recursive_longest_palindromic_subsequence2(seq, i, j) == 2

def test_recursive_longest_palindromic_subsequence4():
    seq = 'BBBBB'
    i = 0
    ans = []
    assert recursive_longest_palindromic_subsequence(seq, i, ans) == 5
    j = len(seq) - 1
    assert recursive_longest_palindromic_subsequence2(seq, i, j) == 5

def test_recursive_longest_palindromic_subsequence5():
    seq = 'BBCBB'
    i = 0
    ans = []
    assert recursive_longest_palindromic_subsequence(seq, i, ans) == 5
    j = len(seq) - 1
    assert recursive_longest_palindromic_subsequence2(seq, i, j) == 5