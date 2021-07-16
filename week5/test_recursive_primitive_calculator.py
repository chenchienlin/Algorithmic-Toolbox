import random
import logging
from week5.recursive_primitive_calculator import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_primitive_calculator1():
    iter = 100
    for _ in range(iter):
        T = random.randint(1, 100)
        assert recursive_primitive_calculator(0, T) == T
        l = construct_recursive_primitive_calculator(0, T)
        assert l[-1] == T