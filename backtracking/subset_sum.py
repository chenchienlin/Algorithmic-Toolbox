import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def subset_sum(X, used, T, curr_sum, round):
    if curr_sum == T:
        return True
    if round == len(X):
        return False
    
    results = []
    # results = [False for _ in range(len(X))]
    for i in range(round, len(X)):
        if i not in used:
            v = X[i]
            curr_sum += v
            if curr_sum <= T:
                used[round] = i
                res = subset_sum(X, used, T, curr_sum, round+1)
            else:
                res = curr_sum == T
            
            results.append(res)
            # results[i] = res
    return True in results

def subset_sum_clean(X, i, T):
    if T == 0:
        return True
    elif T < 0 or i < 0:
        return False
    else:
        w = subset_sum_clean(X, i-1, T-X[i])
        wo = subset_sum_clean(X, i-1, T)
    return w or wo

def construct_subset_sum(X, i, T):
    if T == 0:
        return []
    elif T < 0 or i < 0:
        return None
    else:
        resultw = construct_subset_sum(X, i-1, T-X[i])
        if resultw is not None:
            resultw.append(X[i])
            return resultw
        resultwo = construct_subset_sum(X, i-1, T)
        if resultwo is not None:
            return resultwo
        return None