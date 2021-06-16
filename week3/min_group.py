def min_group_naive(arr):
    has_group = dict()
    for item in arr:
        has_group[item] = False
    groups = list()
    loop_count = 0
    for i in range(0, len(arr)):
        
        if has_group[arr[i]] == True: continue
        loop_count += 1
        new_group = list()
        new_group.append(arr[i])
        maxitem, minitem = arr[i], arr[i]
        for j in range(i+1, len(arr)):
            if has_group[arr[j]] == True: continue
            if abs(maxitem-arr[j]) > 1 or abs(minitem-arr[j]) > 1: continue
            
            loop_count += 1
            new_group.append(arr[j])
            has_group[arr[j]] = True
            
            if arr[j] > maxitem: maxitem = arr[j]
            elif arr[j] < minitem: minitem = arr[j]
        
        groups.append(new_group)
    
    print(f'loop count : {loop_count}')
    return len(groups)

def min_group_sorted(arr):
    groups = list()
    i = 0
    while i < len(arr):
        new_group = list()
        new_group.append(arr[i])
        min = arr[i]
        i += 1
        while i < len(arr):
            if arr[i] <= min + 1:
                new_group.append(arr[i])
                i += 1
            else: break
        groups.append(new_group)
    return len(groups)

arr = [1,1,1,2,3,5]
print(min_group_sorted(arr))