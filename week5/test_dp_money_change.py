import logging
from week5.dp_money_change import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_change1():
    money = 9
    coins = [6,5,1]
    assert dp_money_change(money, coins) == 4
    assert dp_money_change2(money, coins) == 4

def test_recursive_change2():
    money = 40
    coins = [25,20,10,5]
    assert dp_money_change(money, coins) == 2
    assert dp_money_change2(money, coins) == 2

def test_recursive_change3():
    money = 3
    coins = [2]
    assert dp_money_change2(money, coins) == -1