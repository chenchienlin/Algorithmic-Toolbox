import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def dp_k_subset_sum(X, K):
    if sum(X) % K != 0:
        return False
    T = int(sum(X)/K)
    T_list = [T for _ in range(K)]
    i = len(X)-1
    memo = dict()
    return k_subset_sum_helper(X, i, T_list, memo)

def k_subset_sum_helper(X, i, T_list, memo):
    if sum(T_list) == 0:
        return True
    elif i < 0:
        return False
    elif tuple([i, *T_list]) in memo:
        LOGGER.debug('Read memo')
        return memo[tuple((i, *T_list))]
    else:
        for j in range(len(T_list)):
            if T_list[j] >= X[i]:
                T_list[j] -= X[i]
                res = k_subset_sum_helper(X, i-1, T_list, memo)
                T_list[j] += X[i]
                if res is True:
                    memo[tuple([i, *T_list])] = True
                    return True
        memo[tuple([i, *T_list])] = False
        return False