import random
import logging
from week2.fibonacci_number import *
from week2.fibonacci_number_last_digit import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_fib_last_digit():
    iteration = 2000
    for i in range(0, iteration):
        n =  random.randint(0, 20)
        it = iter_fib(n)
        it_last = iter_fib_last_digit(n)
        ma_last = matrix_fib_last_digit(n)
        LOGGER.debug(f'iter_fib : {it}')
        str_it = str(it)
        answer = int(str_it[-1])
        assert answer == it_last == ma_last
        