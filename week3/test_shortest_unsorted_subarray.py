import logging
from week3.shortest_unsorted_subarray import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_shortest_unsorted_subarray1():
    nums = [2,6,4,8,10,9,15]
    assert find_unsorted_subarray(nums) == 5
    assert find_unsorted_subarray2(nums) == 5
    nums = [1,2,3,4]
    assert find_unsorted_subarray(nums) == 0
    assert find_unsorted_subarray2(nums) == 0
    nums = [1]
    assert find_unsorted_subarray(nums) == 0
    assert find_unsorted_subarray2(nums) == 0
    nums = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    assert find_unsorted_subarray(nums) == 6
    assert find_unsorted_subarray2(nums) == 6
    nums = [1,2,3,3,3]
    assert find_unsorted_subarray(nums) == 0
    assert find_unsorted_subarray2(nums) == 0