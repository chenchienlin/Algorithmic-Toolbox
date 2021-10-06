from collections import deque
def permutation(nums):
    nums = deque(nums)
    curr, ans = [], []
    recur_permutation(nums, len(nums), curr, ans)
    return ans

def recur_permutation(nums, i, curr, ans):
    if i == 0:
        ans.append(curr.copy())
    else:
        for j in range(i):
            n = nums.popleft()
            curr.append(n)
            recur_permutation(nums, i-1, curr, ans)
            curr.pop()
            nums.append(n)