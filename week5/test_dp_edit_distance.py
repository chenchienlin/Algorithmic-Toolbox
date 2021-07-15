import logging
from week5.dp_edit_distance import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_edit_distance1():
    str1 = ''
    str2 = 'MONEY'
    assert dp_edit_distance(str1, str2) == len(str2)
    
    str1 = 'FOOD'
    str2 = ''
    assert dp_edit_distance(str1, str2) == len(str1)
    
    str1 = 'FOOD'
    str2 = 'MONEY'
    assert dp_edit_distance(str1, str2) == 4

def test_recursive_edit_distance2():
    str1 = 'cat'
    str2 = 'cut'
    assert dp_edit_distance(str1, str2) == 1

def test_recursive_edit_distance3():
    str1 = 'sunday'
    str2 = 'saturday'
    assert dp_edit_distance(str1, str2) == 3
