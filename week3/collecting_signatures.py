def collecting_signatures(segments):
    A, B = list(), list()
    for seg in segments: 
        A.append(seg[0])
        B.append(seg[1])
    
    zipped_BA = zip(B, A)
    sorted_zipped_BA = sorted(zipped_BA)
    sorted_BA = [list(l) for l in zip(*sorted_zipped_BA)]
    B, A = sorted_BA[0], sorted_BA[1]
    
    bidx, aidx = 0, 0
    points = list()
    
    while True:
        if bidx == len(B)-1: # bidx=0:n-1
            return len(points), points
        else:
            points.append(B[bidx])
            while A[aidx] <= B[bidx]:
                if aidx+1 < len(A): # aidx=0:n-1
                    aidx += 1
                else: break
            bidx = aidx

segments = [[2, 5], [3, 6], [1, 3]]
print(collecting_signatures(segments))

segments = [[4, 7], [1, 3], [2, 5], [5, 6]]
print(collecting_signatures(segments))