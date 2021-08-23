import logging
from week3.maximum_area_of_a_cake import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_maximum_area_of_a_cake1():
    h = 5
    w = 4
    horizontalCuts = [1,2,4]
    verticalCuts = [1,3]
    assert maximum_area_of_a_cake(h, w, horizontalCuts, verticalCuts) == 4

def test_maximum_area_of_a_cake2():
    h = 5
    w = 4
    horizontalCuts = [3,1]
    verticalCuts = [1]
    assert maximum_area_of_a_cake(h, w, horizontalCuts, verticalCuts) == 6

def test_maximum_area_of_a_cake3():
    h = 1000000000
    w = 1000000000
    horizontalCuts = [2]
    verticalCuts = [2]
    assert maximum_area_of_a_cake(h, w, horizontalCuts, verticalCuts) == 81