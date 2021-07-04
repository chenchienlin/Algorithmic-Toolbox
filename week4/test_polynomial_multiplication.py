import logging
from week4.polynomial_multiplication import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_polynomial_multiplication_naive():
    p1 = [3,2,5]
    p2 = [5,1,2]
    assert polynomial_multiplication_naive(p1, p2) == [15,13,33,9,10]

def test_polynomial_multiplication():
    p1 = [1,2,3,4,5,6,7,8]
    p2 = [8,7,6,5,4,3,2,1]
    n = len(p1)
    al = 0
    bl = 0
    assert polynomial_multiplication(p1, p2, n, al, bl) == polynomial_multiplication_naive(p1, p2)