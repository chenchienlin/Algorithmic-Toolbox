def car_fueling(d, m, stops):
    start, idx = 0, 0
    count = 0
    
    while d - start > m:
        # check if next is reachable
        if stops[idx+1] - start  > m:
            print(f'Error')
            return -1
        
        # find the farest reachable stop
        while idx+1 < len(stops):
            if stops[idx+1] - start <= m:
                idx += 1
            else: break
        
        print(f'stopped at {stops[idx]}')
        start = stops[idx]
        count += 1
    return count

d = 950
m = 400
stops = [200, 375, 550, 750]
print(car_fueling(d, m, stops))

d = 10
m = 3
stops = [1, 2, 5, 9]
print(car_fueling(d, m, stops))

d = 200
m = 250
stops = [100, 150]
print(car_fueling(d, m, stops))