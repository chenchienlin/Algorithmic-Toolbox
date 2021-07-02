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

def test_find_greater1():
    arr = [i for i in range(-20,22,2)]
    target = -100
    idx = find_greater(arr, target)
    assert arr[0] == arr[idx]
    
    target = 100
    idx = find_greater(arr, target)
    assert idx == -1

def test_find_greater2():
    arr = [i for i in range(-20,22,2)]
    LOGGER.debug(arr)
    targets = [i for i in range(-21, 21, 2)]
    for i in range(0, len(targets)):
        target = targets.pop(0)
        idx = find_greater(arr, target)
        LOGGER.debug(f'Target: {target} Result: {arr[idx]}')
        assert arr[idx] == arr[i]

def test_find_smaller1():
    arr = [i for i in range(-20,22,2)]
    target = -100
    idx = find_smaller(arr, target)
    assert idx == -1
    
    target = 100
    idx = find_smaller(arr, target)
    assert arr[idx] == arr[len(arr)-1]

def test_organizing_a_lottery1():
    segs = [[2,3], [0,5], [7,10]]
    points = [1,6,11]
    assert organizing_a_lottery(segs, points) == [1,0,0]

def test_organizing_a_lottery2():
    segs = [[-10,10]]
    points = [-100, 100,0]
    assert organizing_a_lottery(segs, points) == [0,0,1]

def test_organizing_a_lottery3():
    segs = [[0,5], [-3,2], [7,10]]
    points = [1,6]
    assert organizing_a_lottery(segs, points) == [2,0]

def test_organizing_a_lottery4():
    segs = [[0,3], [1,3], [3,8]]
    points = [-1,3,8]
    assert organizing_a_lottery(segs, points) == [0,3,1]

def test_organizing_a_lottery5():
    segs = [[1,3], [2,4], [5,7]]
    points = [0,2,5]
    assert organizing_a_lottery(segs, points) == [0,2,1]