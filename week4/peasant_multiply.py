import math

def peasant_multiply(x, y):
    if x == 0:
        return 0
    else:
        x_prime = math.floor(x/2)
        y_prime = y + y
        prod = peasant_multiply(x_prime, y_prime)
        if x % 2 == 1:
            prod += y
        return prod