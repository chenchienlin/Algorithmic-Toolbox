import math
def maximum_salary(integers):
    l1, l2 = list(), list() # l1: list contains integers which only have units digit
    for num in integers:
        if math.log10(num) < 1:
            l1.append(num)
        else:
            l2.append(num)
    
    for num1 in l1:
        assert num1/10 < 1
    
    for num2 in l2:
        assert num2/10 >= 1
    
    l1 = sorted(l1, reverse=True)
    l2 = sorted(l2, reverse=True)
    
    i, j = 0, 0
    maxi, maxj = len(l1), len(l2)
    result = ''
    while i < maxi or j < maxj:
        if i == maxi and j < maxj:
            result = f'{result}{l2[j]}'
            j += 1
        elif i < maxi and j == maxj:
            result = f'{result}{l1[i]}'
            i += 1
        else:
            num1, num2 = l1[i], l2[j]
            num2_fst_digit = int(str(num2)[0])
            
            if num1 < num2_fst_digit:
                result = f'{result}{l2[j]}'
                j += 1
            else:
                result = f'{result}{l1[i]}'
                i += 1
    return int(result)