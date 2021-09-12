import logging
from week3.jump_game import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_jump_game1():
    nums = [2,3,1,1,4]
    assert jump_game(nums) == True

def test_jump_game2():
    nums = [3,2,1,0,4]
    assert jump_game(nums) == False

def test_jump_game3():
    nums = [1,2,3]
    assert jump_game(nums) == True

def test_jump_game4():
    nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8, \
        8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,\
        4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,\
        0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,\
        9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,\
        7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    assert jump_game(nums) == False

def test_jump_game5():
    nums = [1,1,1,0]
    assert jump_game(nums) == True