import logging
from week4.polynomial_multiplication import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_polynomial_multiplication1():
    p1 = [3,2,5]
    p2 = [5,1,2]
    assert polynomial_multiplication_naive(p1, p2) == [15,13,33,9,10]