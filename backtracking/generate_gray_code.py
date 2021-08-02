def func1(n):
    seq = [0 for _ in range(n)]
    for i in range(1, n+1):
        seq[-i] += 1
        seq[-i] %= 2
        print(seq)
        func2(seq, i)

def func2(seq, n):
    for j in range(1, n):
        seq[-j] += 1
        seq[-j] %= 2
        print(seq)
        func2(seq, j)

func1(3)