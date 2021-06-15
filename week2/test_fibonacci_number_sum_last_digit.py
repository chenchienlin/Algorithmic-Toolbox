import random
import logging
from week2.fibonacci_number import *
from week2.fibonacci_number_sum_last_digit import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_fib_sum_last_digit():
    n = 5
    print(fib_sum_last_digit_naive(5))
    iteration = 2000
    for i in range(0, iteration):
        n =  random.randint(0, 20)
        naive_sum = fib_sum_last_digit_naive(n)
        iter_sum = iter_fib_sum_last_digit(n)
        matrix_sum = matrix_fib_sum_last_digit(n)
        assert naive_sum == iter_sum == matrix_sum