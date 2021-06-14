import random
import logging
from week2.fibonacci_number import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_fib():
    iteration = 2000
    for i in range(0, iteration):
        n =  random.randint(0, 20)
        re = recur_fib(n)
        it = iter_fib(n)
        ma = matrix_fib(n)
        LOGGER.info(f'recur_fib: {re}  iter_fib : {it}  matrix_fib : {ma}')
        assert re == it == ma