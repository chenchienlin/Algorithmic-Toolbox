def find_head(nums):
    min_stack = [nums[0]]
    for i in range(1, len(nums)):
        while min_stack and nums[i] < min_stack[-1]:
            min_stack.pop()
        min_stack.append(nums[i])
    j = 0
    for i in range(len(nums)):
        if nums[i] <= min_stack[j]:
            j += 1
        else:
            break
    return i

def find_tail(nums):
    max_stack = [nums[-1]]
    for i in reversed(range(0, len(nums)-1)):
        while max_stack and nums[i] > max_stack[-1]:
            max_stack.pop()
        max_stack.append(nums[i])
    j = 0
    for i in reversed(range(len(nums))):
        if nums[i] >= max_stack[j]:
            j += 1
        else:
            break
    return i

def find_unsorted_subarray(nums):
    head = find_head(nums)
    tail = find_tail(nums)
    return 0 if head >= tail else tail - head + 1


def find_head2(nums):
    min_stack = [0]
    target = len(nums) - 1
    for i in range(1, len(nums)):
        while min_stack and nums[i] < nums[min_stack[-1]]:
            target = min(target, min_stack.pop())
        min_stack.append(i)
    return target

def find_tail2(nums):
    max_stack = [len(nums)-1]
    target = 0
    for i in reversed(range(0, len(nums)-1)):
        while max_stack and nums[i] > nums[max_stack[-1]]:
            target = max(target, max_stack.pop())
        max_stack.append(i)
    return target

def find_unsorted_subarray2(nums):
    head = find_head2(nums)
    tail = find_tail2(nums)
    return 0 if head >= tail else tail - head + 1