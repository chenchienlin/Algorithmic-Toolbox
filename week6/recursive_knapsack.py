def recursive_knapsack_with_repetition(W, weights, values):
    if W == 0:
        return 0
    else:
        best = 0
        for wi, vi in zip(weights, values):
            if wi <= W:
                val = recursive_knapsack_with_repetition(W-wi, weights, values) + vi
                if val > best:
                    best = val
        return best

def construct_recursive_knapsack_with_repetition(W, weights, values):
    if W == 0:
        return [], []
    best = 0
    best_wi = 0
    best_vi = 0
    w, v = None, None
    for wi, vi in zip(weights, values):
        if wi <= W:
            w, v = construct_recursive_knapsack_with_repetition(W-wi, weights, values)
            val = sum(v) + vi
            if val > best:
                best = val
                best_wi = wi
                best_vi = vi
    if w is not None and v is not None:
        w.append(best_wi)
        v.append(best_vi)
        return w, v
    else:
        return [], []

def recursive_knapsack_without_repetition(W, i, weights, values):
    if W == 0 or i == len(weights):
        return 0
    else:
        take = -1
        if weights[i] <= W:
            take = recursive_knapsack_without_repetition(W-weights[i], i+1, weights, values) + values[i]
        skip = recursive_knapsack_without_repetition(W, i+1, weights, values)
        return max(take, skip)

def recursive_knapsack_without_repetition2(W, leni, weights, values):
    if W == 0 or leni == 0:
        return 0
    else:
        take = -1
        if weights[leni-1] <= W:
            take = recursive_knapsack_without_repetition2(W-weights[leni-1], leni-1, weights, values) + values[leni-1]
        skip = recursive_knapsack_without_repetition2(W, leni-1, weights, values)
        return max(take, skip)