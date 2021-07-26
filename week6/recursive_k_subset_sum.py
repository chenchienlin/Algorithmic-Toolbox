def recursive_k_subset_sum(X, i, T_list):
    if sum(T_list) == 0:
        return True
    elif i < 0:
        return False
    else:
        for j in range(len(T_list)):
            if T_list[j] >= X[i]:
                T_list[j] -= X[i]
                res = recursive_k_subset_sum(X, i-1, T_list)
                if res is True:
                    return True
                else:
                    T_list[j] += X[i]
        return False