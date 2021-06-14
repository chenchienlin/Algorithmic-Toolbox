import logging 
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def max_pairwise_product_naive(input_numbers):
    max_prod = 0
    for i in range(0, len(input_numbers)):
        for j in range(i+1, len(input_numbers)):
            LOGGER.debug(f'{i}th x {j}th')
            prod = input_numbers[i] * input_numbers[j]
            if prod > max_prod:
                max_prod = prod
    return max_prod

def max_pairwise_product_sort(input_numbers):
    sorted_numbers = sorted(input_numbers)
    return sorted_numbers[-1] * sorted_numbers[-2]

def max_pairwise_product_linear_scan(input_numbers):
    first_idx, second_idx = -1, -1
    first_max, second_max = 0, 0
    
    for i in range(0, len(input_numbers)):
        if input_numbers[i] > first_max:
            first_idx = i
            first_max = input_numbers[i]
    for j in range(0, len(input_numbers)):
        if input_numbers[j] > second_max and j != first_idx:
            second_idx = j
            second_max = input_numbers[j]
    assert first_idx != second_idx
    return first_max * second_max