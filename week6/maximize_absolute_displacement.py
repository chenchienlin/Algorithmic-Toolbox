def recursive_process_command(seq, i):
    if i == len(seq):
        return 0, 0
    else:
        a, b = recursive_process_command(seq, i+1)
        if seq[i] == 'R':
            return a+1, b+1
        elif seq[i] == 'L':
            return a-1, b-1
        elif seq[i] == '?':
            return a+1, b-1


def recursive_process_command2(seq, i, ans):
    if i == len(seq):
        return ans
    elif seq[i] == 'R':
        return recursive_process_command(seq, i+1, ans+1)
    elif seq[i] == 'L':
        return recursive_process_command(seq, i+1, ans-1)
    elif seq[i] == '?':
        a = recursive_process_command(seq, i+1, ans+1)
        b = recursive_process_command(seq, i+1, ans-1)
        return max(abs(a), abs(b))


def dp_maximize_absolute_displacement(seq):
    Max = [float('-inf') for _ in range(len(seq)+1)]
    Min = [float('inf') for _ in range(len(seq)+1)]
    
    # Recurrence base case
    Max[len(seq)] = 0
    Min[len(seq)] = 0
    for i in reversed(range(len(seq))):
        if seq[i] == 'R':
            Max[i] = Max[i+1] + 1
            Min[i] = Min[i+1] + 1
        elif seq[i] == 'L':
            Max[i] = Max[i+1] - 1
            Min[i] = Min[i+1] - 1
        elif seq[i] == '?':
            Max[i] = Max[i+1] + 1
            Min[i] = Min[i+1] - 1
    return Max[0], Min[0]


def hash_process_command(seq):
    D = dict()
    D['L'] = 0
    D['R'] = 0
    D['?'] = 0
    for elem in seq:
        D[elem] += 1
    return max(abs(D['L'] - D['R']), abs(D['R'] - D['L'])) + D['?']