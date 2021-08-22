import logging
from week4.search_in_rotated_sorted_array import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_search_in_rotated_sorted_array1():
    nums = [4,5,6,7,0,1,2]
    target = 0
    assert search_in_rotated_sorted_array(nums, target) == 4

def test_search_in_rotated_sorted_array2():
    nums = [4,5,6,7,0,1,2]
    target = 3
    assert search_in_rotated_sorted_array(nums, target) == -1

def test_search_in_rotated_sorted_array3():
    nums = [4,5,6,7,0,1,2,3]
    target = 3
    assert search_in_rotated_sorted_array(nums, target) == 7

def test_search_in_rotated_sorted_array4():
    nums = [1]
    target = 0
    assert search_in_rotated_sorted_array(nums, target) == -1

def test_search_in_rotated_sorted_array5():
    nums = [1]
    target = 2
    assert search_in_rotated_sorted_array(nums, target) == -1

def test_search_in_rotated_sorted_array6():
    nums = [1,3]
    target = 3
    assert search_in_rotated_sorted_array(nums, target) == 1

def test_search_in_rotated_sorted_array7():
    nums = [3,1]
    target = 1
    assert search_in_rotated_sorted_array(nums, target) == 1