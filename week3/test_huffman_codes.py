import logging
from week3.huffman_codes import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_build_huffman():
    f = [(5,'f', 0),(9, 'e', 1), (12, 'c', 2), (13, 'b', 3), (16, 'd', 4), (45, 'a', 5)]
    L, R, P = build_huffman2(f)
    print(L, R, P)
    B = list()
    huffman_encode_one(0)