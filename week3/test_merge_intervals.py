import logging
from week3.merge_intervals import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_merge_intervals1():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    assert merge_intervals(intervals) == [[1,6],[8,10],[15,18]]

def test_merge_intervals2():
    intervals = [[1,4],[4,5]]
    assert merge_intervals(intervals) == [[1,5]]

def test_merge_intervals3():
    intervals = [[1,4],[0,4]]
    assert merge_intervals(intervals) == [[0,4]]

def test_merge_intervals4():
    intervals = [[1,4],[4,5]]
    assert merge_intervals(intervals) == [[1,5]]

def test_merge_intervals5():
    intervals = [[1,4],[0,1]]
    assert merge_intervals(intervals) == [[0,4]]

def test_merge_intervals6():
    intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    assert merge_intervals(intervals) == [[1,10]]

