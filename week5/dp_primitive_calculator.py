def dp_primitive_calculator(T):
    # Init memoization data structure
    table = [0 for _ in range(T+1)]
    
    # Recursion base case
    table[0] = 0
    
    # Compute from i=1 to i=T
    for i in range(1, T+1):
        a, b, c = T, T, T
        if i-1 >= 0:
            a = table[i-1] + 1
        if i%2 == 0:
            b = table[int(i/2)] + 1
        if i%3 == 0:
            c = table[int(i/3)] + 1
        table[i] = min(a,b,c)
    l = construct(T, table)
    return l

def construct(T, table):
    i = T
    l = []
    while i > 0:
        if i%3 == 0 and table[i] == table[int(i/3)] + 1:
            l.append(i)
            i = int(i/3)
        elif i%2 == 0 and table[i] == table[int(i/2)] + 1:
            l.append(i)
            i = int(i/2)
        elif i-1 >= 0 and table[i] == table[int(i-1)] + 1:
            l.append(i)
            i -= 1
    list.reverse(l)
    return l