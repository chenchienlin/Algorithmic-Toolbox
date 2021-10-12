import logging
from week6.maximal_square import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_maximal_square1():
    matrix = [  ["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]]
    assert maximal_square(matrix) == 4

def test_maximal_square2():
    matrix = [  ["1","0","1","1","1"],
                ["1","0","1","0","1"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","1"]]
    assert maximal_square(matrix) == 4

def test_maximal_square3():
    matrix = [  ["1","1","1","1","1"],
                ["1","1","1","0","1"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","1"]]
    assert maximal_square(matrix) == 4

def test_maximal_square4():
    matrix = [  ["1","1","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","1"]]
    assert maximal_square(matrix) == 9

def test_maximal_square5():
    matrix = [  ["1","1","1","1","1"],
                ["1","1","1","1","1"],
                ["1","1","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","0","0"]]
    assert maximal_square(matrix) == 16

def test_maximal_square6():
    matrix = [  ["1","1","1","1","0"],
                ["1","1","1","1","0"],
                ["1","1","1","1","1"],
                ["1","1","1","1","1"],
                ["0","0","1","1","1"]]
    assert maximal_square(matrix) == 16