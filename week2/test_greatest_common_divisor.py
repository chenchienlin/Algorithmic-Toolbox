import math
import random
import logging
from week2.greatest_common_divisor import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_gcd_naive():
    iteration = 2000
    for i in range(0, iteration):
        a = random.randint(1, 100) * random.randint(1, 100)
        b = random.randint(1, 100) * random.randint(1, 100)
        gcd = gcd_naive(a, b)
        gcd_eud = gcd_euclidean(a, b)
        gcd_python = math.gcd(a, b)
        LOGGER.info(f'a : {a}  b : {b}')
        LOGGER.info(f'gcd_naive : {gcd}')
        LOGGER.info(f'gcd_euclidean : {gcd_eud}')
        LOGGER.info(f'gcd_python : {gcd_python}')
        assert gcd == gcd_eud == gcd_python