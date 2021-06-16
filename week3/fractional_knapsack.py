def fractional_knapsack(W, wn, vn):
    '''
    W : Remaing wegiht that is available in knapsack
    wn : array stores each weight of items
    vn : array stores each value of items
    '''
    frac = list()
    # compute fraction of each item. O(n)
    for i in range(0, len(wn)):
        frac.append(vn[i]/wn[i])
    amount = list()
    V = 0
    for i in range(0, len(frac)):
        amount.append(0)
    
    while W > 0:
        # find index of max fraction
        best = -1
        max_frac = 0
        for i in range(0, len(frac)):
            if frac[i] > max_frac and wn[i] > 0:
                max_frac = frac[i]
                best = i
        if best == -1: return 'Error'
        a = min(W, wn[best])
        W = W - a
        V = V + a * max_frac
        wn[best] = wn[best] - a
        amount[best] = amount[best] + a

wn = [4, 3, 2]
vn = [20, 18, 14]
W = 7
fractional_knapsack(W, wn, vn)