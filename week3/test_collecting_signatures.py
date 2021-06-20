import logging
from week3.collecting_signatures import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_collecting_signatures1():
    segments = [[2, 5], [3, 6], [1, 3]]
    m, points = collecting_signatures(segments)
    assert m == 1
    assert points == [3]
    

def test_collecting_signatures2():
    segments = [[4, 7], [1, 3], [2, 5], [5, 6]]
    m, points = collecting_signatures(segments)
    assert m == 2
    assert points == [3, 6]