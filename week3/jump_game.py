def jump_game(nums):
    # Each time, choose the farest position with largest number
    pos = 0
    while True:
        if nums[pos] >= (len(nums)-1)-pos:
            return True
        
        # find the index of the best candidate
        best_idx = -1
        best_scr = 0
        for i in range(pos+1, nums[pos]+pos+1):
            scr = (i-pos) + nums[i]
            if scr > best_scr:
                best_scr = scr
                best_idx = i
        
        # If not found
        if best_idx == -1:
            return False
        pos = best_idx