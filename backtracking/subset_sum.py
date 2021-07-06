import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def subset_sum(X, used, T, curr_sum, round):
    if curr_sum == T:
        return True
    if round == len(X):
        return False
    
    results = [False for _ in range(len(X))]
    for i in range(round, len(X)):
        if i not in used:
            v = X[i]
            curr_sum += v
            if curr_sum <= T:
                used[round] = i
                res = subset_sum(X, used, T, curr_sum, round+1)
            else:
                res = curr_sum == T
            results[i] = res
    return True in results