def maximum_advertisement_revenue_wrong(a, b):
    if len(a) == 0 or len(b) == 0: return -1
    value = 0
    while len(a) > 0 and len(b) > 0:
        if len(a) != len(b): return -1
        max_prod = float('-inf')
        besti, bestj = 0, 0
        
        # find the maximum product in two sequences
        for i in range(0, len(a)):
            for j in range(0, len(b)):
                new_prod = a[i] * b[j]
                if new_prod > max_prod:
                    max_prod = new_prod
                    besti, bestj = i, j
        value += max_prod
        
        # remove besti, bestj in a, b
        del a[besti]
        del b[bestj]
    return value

def maximum_advertisement_revenue_sort(a, b):
    if isinstance(a, list) == False and isinstance(b, list) == False:
        return a * b
    
    if len(a) == 0 or len(b) == 0: return None
    if len(a) != len(b): return None
    
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    
    v = sum([a * b for a, b in zip(a, b)])
    
    return v