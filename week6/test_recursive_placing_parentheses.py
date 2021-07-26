import logging
from week6.recursive_placing_parentheses import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_placing_parentheses1():
    nums = [5,8,7,4,8,9]
    ops = ['-','+','*','-','+']
    i = 0
    max, min = recursive_placing_parentheses(nums, ops, i)
    assert max == 200

def test_recursive_placing_parentheses2():
    nums = [1,5]
    ops = ['+']
    i = 0
    max, min = recursive_placing_parentheses(nums, ops, i)
    assert max == 6
    assert min == 6

def test_recursive_placing_parentheses3():
    nums = [1,2,3,4,5]
    ops = ['+','*','+','*']
    i = 0
    max, min = recursive_placing_parentheses(nums, ops, i)
    assert max == 105
    assert min == 27