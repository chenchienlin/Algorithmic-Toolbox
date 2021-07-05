import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def recursive_change(money, coins):
    if money == 0:
        return 0
    min_num_coins = float('inf')
    for c in coins:
        if money-c >= 0:
            n = recursive_change(money-c, coins) + 1
            if n < min_num_coins:
                min_num_coins = n
    return min_num_coins