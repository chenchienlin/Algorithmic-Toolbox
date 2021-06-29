def polynomial_multiplication_naive(p1, p2):
    result = [0 for _ in range( len(p1) + len(p2) -1 )]
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i+j] += p1[i] * p2[j]
    return result