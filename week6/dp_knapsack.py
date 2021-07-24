def dp_knapsack_with_repetition(W, weights, values):
    # Init memoization data structure
    table = [-1 for _ in range(W+1)]
    
    # Compute recurence base case
    table[0] = 0
    
    # Compute from i=0:len(weights) w=1:W
    for i in range(len(weights)):
        for w in range(1, W+1):
            if weights[i] <= w:
                val = table[w-weights[i]] + values[i]
                if val > table[w]:
                    table[w] = val
    
    # Reconstruct solution
    curr = W
    ws = []
    vs = []
    while curr > 0:
        for i in range(len(weights)):
            if curr-weights[i] >= 0:
                if table[curr-weights[i]] + values[i] == table[curr]:
                    curr -= weights[i]
                    ws.append(weights[i])
                    vs.append(values[i])
    assert curr == 0
    return table[W], ws, vs

def dp_knapsack_without_repetition(W, weights, values):
    # Init memoization data structure
    table = [[-1 for _ in range(W+1)] for _ in range(len(weights)+1)]
    
    # Compute recurence base case
    for row in range(len(weights)+1):
        table[row][0] = 0
    
    for col in range(W+1):
        table[0][col] = 0
    
    # Compute from i=1:len(weights) w=1:W
    for i in range(1, len(weights)+1):
        for w in range(1, W+1):
            table[i][w] = table[i-1][w]
            if weights[i-1] <= w:
                val = table[i-1][w-weights[i-1]] + values[i-1]
                if val > table[i][w]:
                    table[i][w] = val
    
    # Reconstruct solution
    curri = len(weights)
    currw = W
    ws = []
    vs = []
    while curri > 0:
        idx = curri - 1
        if table[curri][currw-weights[idx]] + values[idx] == table[curri][currw]:
            ws.append(weights[idx])
            vs.append(values[idx])
            currw -= weights[idx]
        curri -= 1
    return table[len(weights)][W], ws, vs