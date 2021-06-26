import logging
from week4.majority_element import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_majority_element1():
    arr = [2,3,9,2,2]
    assert majority_element_voting(arr) == 2

def test_majority_element2():
    arr = [1,2,3,4]
    assert majority_element_voting(arr) == None

def test_majority_element3():
    arr = [1,2,3,1]
    assert majority_element_voting(arr) == None