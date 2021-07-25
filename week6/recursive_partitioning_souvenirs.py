import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def recursive_partitioning_souvenirs(X, i, Ta, Tb, Tc):
    if Ta == 0 and Tb == 0 and Tc == 0:
        return True
    elif Ta < 0 or Tb < 0 or Tc < 0 or i < 0:
        return False
    else:
        a, b, c = False, False, False
        a = recursive_partitioning_souvenirs(X, i-1, Ta-X[i], Tb, Tc)
        if a is False:
            b = recursive_partitioning_souvenirs(X, i-1, Ta, Tb-X[i], Tc)
        if a is False and b is False:
            c = recursive_partitioning_souvenirs(X, i-1, Ta, Tb, Tc-X[i])
        return a or b or c