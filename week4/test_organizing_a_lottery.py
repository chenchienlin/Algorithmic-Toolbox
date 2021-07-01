import logging
from week4.organizing_a_lottery import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_organizing_a_lottery_naive1():
    segs = [[2,3], [0,5], [7,10]]
    points = [1,6,11]
    assert organizing_a_lottery_naive(segs, points) == [1,0,0]

def test_organizing_a_lottery_naive2():
    segs = [[-10,10]]
    points = [-100, 100,0]
    assert organizing_a_lottery_naive(segs, points) == [0,0,1]

def test_organizing_a_lottery_naive3():
    segs = [[0,5], [-3,2], [7,10]]
    points = [1,6]
    assert organizing_a_lottery_naive(segs, points) == [2,0]