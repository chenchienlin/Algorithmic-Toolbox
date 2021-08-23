def maximum_area_of_a_cake(h, w, horizontalCuts, verticalCuts):
    if horizontalCuts[0] != 0:
        horizontalCuts.insert(0, 0)
    if horizontalCuts[-1] != h:
        horizontalCuts.append(h)
    if verticalCuts[0] != 0:
        verticalCuts.insert(0, 0)
    if verticalCuts[-1] != w:
        verticalCuts.append(w)
    horizontalCuts.sort()
    verticalCuts.sort()
    x_interval, y_interval = 0, 0
    for i in range(len(horizontalCuts)-1):
        if abs(horizontalCuts[i] - horizontalCuts[i+1]) > y_interval:
            y_interval = abs(horizontalCuts[i] - horizontalCuts[i+1])
    for j in range(len(verticalCuts)-1):
        if abs(verticalCuts[j] - verticalCuts[j+1]) > x_interval:
            x_interval = abs(verticalCuts[j] - verticalCuts[j+1])
    # Since the answer can be a large number, return this modulo 10^9 + 7
    return int(x_interval * y_interval) % (10**9+7)