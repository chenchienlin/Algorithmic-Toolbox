import random
import logging
from week3.maximum_advertisement_revenue import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_maximum_advertisement_revenue():
    a = 23
    b = 39
    assert maximum_advertisement_revenue_sort(a, b) == 897

def test_maximum_advertisement_revenue2():
    a = [1, 3, -5]
    b = [-2, 4, 1]
    assert maximum_advertisement_revenue_sort(a, b) == 23