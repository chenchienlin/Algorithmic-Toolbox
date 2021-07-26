def recursive_k_subset_sum(X, K):
    if sum(X) % K != 0:
        return False
    T = int(sum(X)/K)
    T_list = [T for _ in range(K)]
    i = len(X)-1
    return  k_subset_sum_helper(X, i, T_list)

def k_subset_sum_helper(X, i, T_list):
    if sum(T_list) == 0:
        return True
    elif i < 0:
        return False
    else:
        for j in range(len(T_list)):
            if T_list[j] >= X[i]:
                T_list[j] -= X[i]
                res = k_subset_sum_helper(X, i-1, T_list)
                if res is True:
                    return True
                else:
                    T_list[j] += X[i]
        return False