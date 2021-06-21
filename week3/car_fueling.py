def car_fueling(d, m, stops):
    start, idx, count = 0, 0, 0
    while d - start > m:
        
        # find the farest reachable gas stop
        while idx+1 < len(stops):
            if stops[idx+1] - start <= m: # if the next stop is reachable
                idx += 1
            else: break
        
        # check reachability 
        # if idx is not increased, meaning cannot find reachable stop
        if stops[idx] == start:
            return -1
        
        count += 1
        start = stops[idx]
    return count