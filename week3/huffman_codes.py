import heapq

class Node:
    def __init__(self, left, right, freq):
        self.left = left
        self.right = right
        self.freq = freq

def build_huffman(f):
    heapq.heapify(f)
    for i in range(1, len(f)): # i = 1:len(f)-1
        tup_x = heapq.heappop(f)
        tup_y = heapq.heappop(f)
        freq_x, x = tup_x[0], tup_x[1]
        freq_y, y = tup_y[0], tup_y[1]
        new_freq = freq_x + freq_y
        node = Node(tup_x, tup_y, new_freq)
        heapq.heappush(f, (new_freq, node))
    return heapq.heappop(f)

def build_huffman2(f):
    pq = f.copy()
    heapq.heapify(pq)
    L = [0 for i in range(0, len(pq))]
    R = [0 for i in range(0, len(pq))]
    P = [0 for i in range(0, 2*len(pq)-1)]
    for i in range(len(pq), 2*len(pq)-1):
        tup_x = heapq.heappop(pq)
        tup_y = heapq.heappop(pq)
        freq_x, x, x_idx = tup_x[0], tup_x[1], tup_x[2]
        freq_y, y, y_idx = tup_y[0], tup_y[1], tup_y[2]
        new_freq = freq_x + freq_y
        heapq.heappush(pq, (new_freq, f'{x}{y}', i))
        L.append(x_idx)
        R.append(y_idx)
        P[x_idx] = i
        P[y_idx] = i
    return L, R, P

def huffman_encode_one(x, f, L, P, B):
    if x < 2 * len(f) - 2:
        huffman_encode_one(P[x])
        if x == L[P[x]]:
            B.append(0)
        else:
            B.append(1)