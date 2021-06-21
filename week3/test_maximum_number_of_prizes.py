import logging
from week3.maximum_number_of_prizes import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_maximum_number_of_prizes1():
    assert maximum_number_of_prizes(6, 1) == [6]
    assert maximum_number_of_prizes(6, 2) == [1, 5]
    assert maximum_number_of_prizes(6, 3) == [1, 2, 3]
    assert maximum_number_of_prizes(6, 4) == -1
    assert maximum_number_of_prizes(6, 5) == -1
    assert maximum_number_of_prizes(6, 6) == -1
    assert maximum_number_of_prizes(6, 7) == -1

def test_maximum_number_of_prizes2():
    assert maximum_number_of_prizes(8, 1) == [8]
    assert maximum_number_of_prizes(8, 2) == [1, 7]
    assert maximum_number_of_prizes(8, 3) == [1, 2, 5]
    assert maximum_number_of_prizes(8, 4) == -1
    assert maximum_number_of_prizes(8, 5) == -1
    assert maximum_number_of_prizes(8, 6) == -1
    assert maximum_number_of_prizes(8, 7) == -1
    assert maximum_number_of_prizes(8, 8) == -1

def test_maximum_number_of_prizes3():
    assert maximum_number_of_prizes(2, 1) == [2]
    assert maximum_number_of_prizes(2, 2) == -1

