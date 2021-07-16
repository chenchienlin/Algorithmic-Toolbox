def recursive_primitive_calculator(num, T):
    if num > T:
        return -1
    elif num == T:
        return num
    elif num == 0:
        return recursive_primitive_calculator(num+1, T)
    else:
        a = recursive_primitive_calculator(num+1, T)
        b = recursive_primitive_calculator(num*2, T)
        c = recursive_primitive_calculator(num*3, T)
        return max(a, b, c)

def construct_recursive_primitive_calculator(num, T):
    if num > T:
        return None
    elif num == T:
        return []
    elif num == 0:
        a = construct_recursive_primitive_calculator(num+1, T)
        if a != None:
            a.insert(0, num+1)
            return a
    else:
        c = construct_recursive_primitive_calculator(num*3, T)
        if c != None:
            c.insert(0, num*3)
            return c
        
        b = construct_recursive_primitive_calculator(num*2, T)
        if b != None:
            b.insert(0, num*2)
            return b
        
        a = construct_recursive_primitive_calculator(num+1, T)
        if a != None:
            a.insert(0, num+1)
            return a