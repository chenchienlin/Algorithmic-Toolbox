import math
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def polynomial_multiplication_naive(p1, p2):
    result = [0 for _ in range( len(p1) + len(p2) -1 )]
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i+j] += p1[i] * p2[j]
    return result

# works when p1 and p2 have even number of terms
def polynomial_multiplication(p1, p2, n, al, bl):
    res = [0 for _ in range(0, 2*n-1)]
    if n == 1:
        res[0] = p1[al] * p2[bl]
        return res
    n2 = math.ceil(n/2)
    res[0:n-2 + 1] = polynomial_multiplication(p1, p2, n2, al, bl)
    res[n:2*n-2 + 1] = polynomial_multiplication(p1, p2,n2, al + n2, bl + n2)
    D0E0 = polynomial_multiplication(p1, p2, n2, al, bl)
    D1E1 = polynomial_multiplication(p1, p2,n2, al + n2, bl + n2)
    D0E1 = polynomial_multiplication(p1, p2, n2, al, bl + n2)
    D1E0 = polynomial_multiplication(p1, p2, n2, al + n2, bl)
    LOGGER.debug(f'D0E0 {D0E0}')
    LOGGER.debug(f'D1E1 {D1E1}')
    LOGGER.debug(f'D0E1 {D0E1}')
    LOGGER.debug(f'D1E0 {D1E0}')
    res[n2:n+n2-2 + 1] = [a + b for a, b in zip(res[n2:n+n2-2 + 1], D0E1)]
    res[n2:n+n2-2 + 1] = [a + b for a, b in zip(res[n2:n+n2-2 + 1], D1E0)]
    return res