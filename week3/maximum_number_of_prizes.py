def maximum_number_of_prizes(n, k):
    A = list()
    a = 1
    
    while k > 1:
        n -= a
        A.append(a)
        
        if n <= a: 
            return -1
        
        a += 1
        k -= 1
    
    if k == 1:
        A.append(n)
        return A