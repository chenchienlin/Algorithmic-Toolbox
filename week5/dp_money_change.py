
def dp_money_change(money, coins):
    table = [[0 for _ in range(money+1)] for _ in range(len(coins)+1)]
    for col in range(1, money+1):
        table[0][col] = money
    
    for ci in range(1, len(coins)+1):
        c = coins[ci-1]
        for mi in range(1, money+1):
            table[ci][mi] = table[ci-1][mi]
            if mi >= c:
                new = table[ci][mi-c] + 1
                if new < table[ci][mi]:
                    table[ci][mi] = new
    
    return table[len(coins)][money]