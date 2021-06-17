def recur_money_change(money, coins):
    l = list()
    recur_money_change_helper(money, coins, l)
    print(l)
    return len(l)

def recur_money_change_helper(money, coins, l):
    if money == 0: return
    
    # find maximum coins[i] so that coins[i] <= money (greedy choice)
    i = 0
    for j in range(i+1, len(coins)):
        if coins[j] <= money:
            i = j
    
    money = money - coins[i]
    l.append(coins[i])
    print(f'add one {coins[i]} coin')
    recur_money_change_helper(money, coins, l)


def iter_money_change(money, coins):
    if money == 0: return 0
    
    l = list()
    
    while money > 0:
        i = 0
        for j in range(0, len(coins)):
            if coins[j] <= money:
                i = j
        
        money = money - coins[i]
        l.append(coins[i])
        print(f'add one {coins[i]} coin')
    print(l)
    return len(l)

money = 28
coins = [1, 5, 10]
recur_money_change(money, coins)
iter_money_change(money, coins)