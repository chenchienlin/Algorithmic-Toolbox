import logging
from backtracking.generate_parentheses import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_generate_parentheses():
    i = j = 0
    n = 1
    assert generate_parentheses(n, i, j) == ["()"]
    n = 2
    assert generate_parentheses(n, i, j) == ['(())', '()()']
    n = 3
    assert generate_parentheses(n, i, j) == ["((()))","(()())","(())()","()(())","()()()"]