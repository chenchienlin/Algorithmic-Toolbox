import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def dp_partitioning_souvenirs(X, i, Ta, Tb, Tc, memo):
    if Ta == 0 and Tb == 0 and Tc == 0:
        return True
    elif Ta < 0 or Tb < 0 or Tc < 0 or i < 0:
        return False
    elif (i, Ta, Tb, Tc) in memo:
        return memo[(i, Ta, Tb, Tc)]
    else:
        a, b, c = False, False, False
        a = dp_partitioning_souvenirs(X, i-1, Ta-X[i], Tb, Tc, memo)
        if a is False:
            b = dp_partitioning_souvenirs(X, i-1, Ta, Tb-X[i], Tc, memo)
        if a is False and b is False:
            c = dp_partitioning_souvenirs(X, i-1, Ta, Tb, Tc-X[i], memo)
        result = a or b or c
        memo[(i, Ta, Tb, Tc)] = result
        return memo[(i, Ta, Tb, Tc)]

X = [17,59,34,57,17,23,67,1,18,2,59]
i = len(X)-1
T = int(sum(X)/3)
print(dp_partitioning_souvenirs(X, i, T, T, T, dict()))
