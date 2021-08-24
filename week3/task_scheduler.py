def task_scheduler(tasks, n):
    freq = dict()
    for t in tasks: 
        freq[t] = freq.get(t, 0)+1
    freq = sorted(freq.items(), key=lambda elem:elem[1])
    chr, f_max = freq.pop()
    idle_task = (f_max - 1) * n
    
    while freq and idle_task > 0:
        chr, f = freq.pop()
        if f == f_max:
            idle_task -= (f_max-1)
        else:
            idle_task -= f
    
    if idle_task <= 0:
        return len(tasks)
    else:
        return len(tasks) + idle_task