def permutation_composition(a, b):
    assert len(a) == len(b)
    return [b[a[k] - 1] for k in range(len(a))]


# a = [5,3,1,4,2]
# b = [5,3,2,1,4]
# print(permutation_composition(a, b))


