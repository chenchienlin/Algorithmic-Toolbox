def compute_values(nums, ops,i, j):
    idx = i
    curr = nums[i]
    while idx+1 <= j:
        if ops[idx] == '+':
            curr += nums[idx+1]
        elif ops[idx] == '-':
            curr -= nums[idx+1]
        elif ops[idx] == '*':
            curr *= nums[idx+1]
        elif ops[idx] == '/':
            curr /= nums[idx+1]
        idx += 1    
    return curr

def compute(ops, i, a, b):
    if ops[i] == '+':
        return a + b
    elif ops[i] == '-':
        return a - b
    elif ops[i] == '*':
        return a * b
    elif ops[i] == '/':
        return a / b

def recursive_placing_parentheses(nums, ops, i):
    if i == len(nums)-1:
        return nums[i], nums[i]
    else:
        max = float('-inf')
        min = float('inf')
        for j in range(i, len(nums)-1):
            a = compute_values(nums, ops,i, j)
            ret_max, ret_min = recursive_placing_parentheses(nums, ops, j+1)
            v1 = compute(ops, j, a, ret_max)
            v2 = compute(ops, j, a, ret_min)
            if v1 > max:
                max = v1
            if v2 > max:
                max = v2
            if v1 < min:
                min = v1
            if v2 < min:
                min = v2
        return max, min