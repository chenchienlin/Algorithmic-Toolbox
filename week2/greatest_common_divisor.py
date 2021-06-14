import logging 
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def gcd_naive(a, b):
    best = 0
    for d in range(1, min(a,b)+1):
    # for d in range(1, a+b):
        if a%d == 0 and b%d ==0:
            best = d
    return best

def gcd_euclidean(a, b):
    if b == 0:
        return a
    else:
        a_prime = a % b
    return gcd_euclidean(b, a_prime)