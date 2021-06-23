def greedy_scheduling(S, F):
    zipped_lists = zip(F, S)
    sorted_zipped_lists = sorted(zipped_lists)
    sorted_lists = [list(tup) for tup in zip(*sorted_zipped_lists)]
    F = sorted_lists[0]
    S = sorted_lists[1]
    
    fst_fin = F[0]
    
    schedule = list()
    schedule.append((S[0], F[0]))
    
    for i in range(1, len(S)):
        # Assume people can join different activities continuously.
        if S[i] >= fst_fin:
            schedule.append((S[i], F[i]))
            fst_fin = F[i]
    return schedule