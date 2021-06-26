import logging
from week4.binear_search import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_binary_search():
    l = [1,5,8,12,13]
    for i in range(0, len(l)):
        assert binary_search(l, l[i]) == i
        assert iter_binary_search(l, l[i]) == i
    
    assert binary_search(l, 0) == -1
    assert iter_binary_search(l, 0) == -1
    
    assert binary_search(l, 6) == -1
    assert iter_binary_search(l, 6) == -1
    
    assert binary_search(l, 11) == -1
    assert iter_binary_search(l, 11) == -1
    
    assert binary_search(l, 14) == -1
    assert iter_binary_search(l, 14) == -1