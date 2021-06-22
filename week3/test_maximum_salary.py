import logging
from week3.maximum_salary import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_maximum_salary1():
    integers = [21, 2]
    assert maximum_salary(integers) == 221

def test_maximum_salary2():
    integers = [9, 4, 6, 1, 9]
    assert maximum_salary(integers) == 99641

def test_maximum_salary3():
    integers = [23, 39, 92]
    assert maximum_salary(integers) == 923923