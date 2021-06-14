import random
import logging
from week1.max_pairwise_product import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_max_pairwise_product_naive():
    s = 100
    l = list()
    for i in range(0, s):
        l.append(i)
    random.shuffle(l)
    
    max_prod_naive = max_pairwise_product_naive(l)
    max_prod_sort =  max_pairwise_product_sort(l)
    max_prod_linear_scan = max_pairwise_product_linear_scan(l)
    LOGGER.info(f'max_prod_naive : {max_prod_naive}')
    LOGGER.info(f'max_prod_sort : {max_prod_sort}')
    LOGGER.info(f'max_prod_linear_scan : {max_prod_linear_scan}')
    assert max_prod_naive == max_prod_sort == max_prod_linear_scan