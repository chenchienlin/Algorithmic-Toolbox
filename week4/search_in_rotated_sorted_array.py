def search_in_rotated_sorted_array(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = int( (lo + hi) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[lo]:
            if target >= nums[lo] and target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if target <= nums[hi] and target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1