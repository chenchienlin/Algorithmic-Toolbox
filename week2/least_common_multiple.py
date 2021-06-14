import math
from week2.greatest_common_divisor import gcd_euclidean

def lcm_naive(a,b):
    result = 1
    while True:
        gcd = gcd_euclidean(a, b)
        result *= gcd
        a = int(a / gcd)
        b = int(b / gcd)
        if gcd == 1:
            result *= a
            result *= b
            break
    return result

def lcm(a,b):
    return abs(a*b) // gcd_euclidean(a, b)

def lcm_python(a, b):
    return abs(a*b) // math.gcd(a, b)