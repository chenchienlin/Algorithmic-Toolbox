import logging
from week3.meeting_rooms2 import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_meeting_rooms2_1():
    intervals = [[0,30],[5,10],[15,20]]
    assert meeting_rooms2(intervals) == 2

def test_meeting_rooms2_2():
    intervals = [[11,14],[5,10],[15,20]]
    assert meeting_rooms2(intervals) == 1

def test_meeting_rooms2_3():
    intervals = [[10,15],[5,10],[15,20]]
    assert meeting_rooms2(intervals) == 1

def test_meeting_rooms2_4():
    intervals = [[7,10],[2,4]]
    assert meeting_rooms2(intervals) == 1

def test_meeting_rooms2_5():
    intervals = [[1,5],[8,9],[8,9]]
    assert meeting_rooms2(intervals) == 2

def test_meeting_rooms2_6():
    intervals = [[2,11],[6,16],[11,16]]
    assert meeting_rooms2(intervals) == 2

def test_meeting_rooms2_7():
    intervals = [[2,15],[36,45],[9,29],[16,23],[4,9]]
    assert meeting_rooms2(intervals) == 2