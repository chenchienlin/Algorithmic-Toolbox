import logging
from week6.recursive_valid_parenthesis_string import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_valid_parenthesis_string1():
    s = "()"
    i = 0 
    count = 0
    assert recursive_valid_parenthesis_string(s, i, count) == True

def test_recursive_valid_parenthesis_string2():
    s = "(*)"
    i = 0 
    count = 0
    assert recursive_valid_parenthesis_string(s, i, count) == True

def test_recursive_valid_parenthesis_string3():
    s = "(*))"
    i = 0 
    count = 0
    assert recursive_valid_parenthesis_string(s, i, count) == True


def test_recursive_valid_parenthesis_string4():
    s = "()))"
    i = 0 
    count = 0
    assert recursive_valid_parenthesis_string(s, i, count) == False

def test_recursive_valid_parenthesis_string5():
    s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
    i = 0 
    count = 0
    assert recursive_valid_parenthesis_string(s, i, count) == True