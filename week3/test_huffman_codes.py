import logging
from week3.huffman_codes import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_build_huffman():
    f = [(5,'f', 0),(9, 'e', 1), (12, 'c', 2), (13, 'b', 3), (16, 'd', 4), (45, 'a', 5)]
    L, R, P = build_huffman2(f)
    assert huffman_encode(0, f, L, P) == [1,1,0,0]
    assert huffman_encode(1, f, L, P) == [1,1,0,1]
    assert huffman_encode(2, f, L, P) == [1,0,0]
    assert huffman_encode(3, f, L, P) == [1,0,1]
    assert huffman_encode(4, f, L, P) == [1,1,1]