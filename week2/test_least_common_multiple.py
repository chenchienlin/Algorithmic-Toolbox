import math
import random
import logging
from week2.least_common_multiple import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_gcd():
    iteration = 2000
    for i in range(0, iteration):
        a = random.randint(1, 100) * random.randint(1, 100)
        b = random.randint(1, 100) * random.randint(1, 100)
        lcm1 = lcm_naive(a, b)
        lcm2 = lcm(a, b)
        lcm3 = lcm_python(a, b)
        LOGGER.info(f'a : {a}  b : {b}')
        LOGGER.info(f'lcm_naive : {lcm1}')
        LOGGER.info(f'lcm : {lcm2}')
        LOGGER.info(f'lcm_python : {lcm3}')
        assert lcm1 == lcm2 == lcm3