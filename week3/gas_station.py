def gas_station(gas, cost):
    score = [x1 - x2 for (x1, x2) in zip(gas, cost)]
    if sum(score) < 0:
        return -1
    curr_tank = 0
    start_idx = 0
    for i in range(len(score)):
        curr_tank += score[i]
        if curr_tank < 0:
            start_idx = i + 1
            curr_tank = 0
    return start_idx