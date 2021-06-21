import logging
from week3.car_fueling import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_car_fueling1():
    d = 950
    m = 400
    stops = [200, 375, 550, 750]
    car_fueling(d, m, stops) == 2

def test_car_fueling2():
    d = 10
    m = 3
    stops = [1, 2, 5, 9]
    car_fueling(d, m, stops) == -1

def test_car_fueling3():
    d = 200
    m = 250
    stops = [100, 150]
    car_fueling(d, m, stops) == 0