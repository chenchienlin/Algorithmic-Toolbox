def organizing_a_lottery_naive(segs, points):
    b = []
    for p in points:
        in_range = int(check_in_a_range(p, segs))
        b.append(in_range)
    return b

def check_in_a_range(p, segs):
    in_range = 0
    for seg in segs:
        head = seg[0]
        tail = seg[1]
        if p >= head and p <= tail:
            in_range += 1
    return in_range