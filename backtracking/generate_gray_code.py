def func1(n):
    seq = [0 for _ in range(n)]
    result = []
    for i in range(1, n+1):
        seq[-i] += 1
        seq[-i] %= 2
        result.append(tuple(seq))
        res = func2(seq, i)
        result.extend(tuple(res))
    print(result)

def func2(seq, n):
    result = []
    for j in range(1, n):
        seq[-j] += 1
        seq[-j] %= 2
        result.append(tuple(seq))
        res = func2(seq, j)
        result.extend(tuple(res))
    return result