def meeting_rooms2(intervals):
    intervals.sort(key=lambda x:x[0])
    rooms_end = [intervals[0][1]]
    for i in range(1, len(intervals)):
        # Find the room ends first
        frt_end_idx = 0
        for end_idx in range(len(rooms_end)):
            if rooms_end[end_idx] < rooms_end[frt_end_idx]:
                frt_end_idx = end_idx
        
        # If the candiate room ends before the meeting starts
        if intervals[i][0] >= rooms_end[frt_end_idx]:
            rooms_end[frt_end_idx] = intervals[i][1]
        else:
            rooms_end.append(intervals[i][1])
    return len(rooms_end)