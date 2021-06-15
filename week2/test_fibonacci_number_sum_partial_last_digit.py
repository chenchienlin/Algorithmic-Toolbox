import random
import logging
from week2.fibonacci_number import *
from week2.fibonacci_number_sum_partial_last_digit import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_fib_sum_last_digit():
    iteration = 2000
    for i in range(0, iteration):
        lo = random.randint(0, 20)
        hi = lo + random.randint(0, 5)
        naive_sum = fib_sum_partial_last_digit_naive(lo, hi)
        iter_sum = iter_fib_sum_partial_last_digit(lo, hi)
        matrix_sum = matrix_fib_sum_partial_last_digit(lo, hi)
        assert naive_sum == iter_sum == matrix_sum