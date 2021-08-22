import logging
from week3.valid_palindrome2 import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_valid_palindrome2_1():
    s = "aba"
    assert valid_palindrome2(s) == True

def test_valid_palindrome2_2():
    s = "abca"
    assert valid_palindrome2(s) == True

def test_valid_palindrome2_3():
    s = "cabadc"
    assert valid_palindrome2(s) == True

def test_valid_palindrome2_4():
    s = "abc"
    assert valid_palindrome2(s) == False

def test_valid_palindrome2_5():
    s = "cabadbc"
    assert valid_palindrome2(s) == False