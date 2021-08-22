def merge_intervals(intervals):
    intervals = sorted(intervals)
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] > result[-1][1]:
            result.append(intervals[i])
        else:
            result[-1][1] = max(intervals[i][1], result[-1][1])
    return result