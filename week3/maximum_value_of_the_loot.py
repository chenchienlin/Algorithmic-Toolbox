# Exactly the same with fractional knapsack problem
def maximum_value_of_the_loot(W, wn, vn):
    frac = [x/y for x, y in zip(vn, wn)]
    amount = dict()
    V = 0
    
    zipped_list = zip(frac, wn, vn)
    sorted_zipped_list = sorted(zipped_list, reverse=True)
    sorted_list = [list(l) for l in zip(*sorted_zipped_list)]
    frac, wn, vn = sorted_list[0], sorted_list[1], sorted_list[2]
    
    idx = 0
    while W > 0:
        a = min(W, wn[idx])
        amount[vn[idx]] = a
        
        W -= a
        wn[idx] -= a
        V += a*frac[idx]
        
        idx += 1
    return V

wn = [20, 50, 30]
vn = [60, 100, 120]
W = 50
print(maximum_value_of_the_loot(W, wn, vn))