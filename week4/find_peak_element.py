def find_peak_element(nums):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = int( (lo+hi)/2 )
        # Check if mid is a peak
        left = nums[mid-1] if mid-1 >= 0 else float('-inf')
        right = nums[mid+1] if mid+1 <= hi else float('-inf')
        if nums[mid] > left and nums[mid] > right:
            return mid
        elif left > nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
nums = [1,2,3,1]
print(find_peak_element(nums))

nums = [5, 10, 20, 15]
print(find_peak_element(nums))


nums = [1,2,1,3,5,6,4]
print(find_peak_element(nums))

nums = [10, 20, 15, 2, 23, 90, 67]
print(find_peak_element(nums))

nums = [8, 9, 10, 2, 5, 6]
print(find_peak_element(nums))

nums = [8, 9, 10, 12, 15]
print(find_peak_element(nums))

nums = [10, 8, 6, 5, 3, 2]
print(find_peak_element(nums))