import logging
from week3.greedy_scheduling import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_greedy_scheduling1():
    S = [1,3,0,5,8,5]
    F = [2,4,6,7,9,9]
    assert len(greedy_scheduling(S, F)) == 4

def test_greedy_scheduling2():
    S = [10, 12, 20]
    F = [20, 25, 30]
    assert len(greedy_scheduling(S, F)) == 2
