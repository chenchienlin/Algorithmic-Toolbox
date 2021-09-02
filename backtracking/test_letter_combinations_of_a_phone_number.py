import logging
from backtracking.letter_combinations_of_a_phone_number import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_letter_combinations_of_a_phone_number1():
    digits = "2"
    assert letter_combinations(digits) == ["a","b","c"]
    digits = "23"
    assert letter_combinations(digits) == ["ad","ae","af","bd","be","bf","cd","ce","cf"]