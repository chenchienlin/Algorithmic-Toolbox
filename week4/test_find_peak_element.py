import logging
from week4.find_peak_element import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_find_peak_element1():
    nums = [1,2,3,1]
    assert find_peak_element(nums) == 2

def test_find_peak_element2():
    nums = [5, 10, 20, 15]
    assert find_peak_element(nums) == 2

def test_find_peak_element3():
    nums = [1,2,1,3,5,6,4]
    assert find_peak_element(nums) == 5

def test_find_peak_element4():
    nums = [10, 20, 15, 2, 23, 90, 67]
    assert find_peak_element(nums) == 1

def test_find_peak_element5():
    nums = [8, 9, 10, 2, 5, 6]
    assert find_peak_element(nums) == 2

def test_find_peak_element6():
    nums = [8, 9, 10, 12, 15]
    assert find_peak_element(nums) == 4
    print(find_peak_element(nums))

def test_find_peak_element7():
    nums = [10, 8, 6, 5, 3, 2]
    assert find_peak_element(nums) == 0