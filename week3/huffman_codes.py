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