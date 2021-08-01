import logging
from week6.recursive_wildcard_pattern_matching import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_recursive_wildcard_pattern_matching1():
    pattern = '?arl'
    string = 'Karl'
    assert recursive_wildcard_pattern_matching(string, pattern, i=0, j=0) == True
    
    string = 'Kurl'
    assert recursive_wildcard_pattern_matching(string, pattern, i=0, j=0) == False
    
    string = 'Carl'
    assert recursive_wildcard_pattern_matching(string, pattern, i=0, j=0) == True
    
    string = 'Kur'
    assert recursive_wildcard_pattern_matching(string, pattern, i=0, j=0) == False
    
    string = 'Karll'
    assert recursive_wildcard_pattern_matching(string, pattern, i=0, j=0) == False
    
    string = ''
    assert recursive_wildcard_pattern_matching(string, pattern, i=0, j=0) == False

def test_recursive_wildcard_pattern_matching2():
    string = "baaabab"
    
    pattern = "*****ba*****ab"
    assert recursive_wildcard_pattern_matching2(string, pattern, i=0, j=0) == True
    
    pattern = "baaa?ab"
    assert recursive_wildcard_pattern_matching2(string, pattern, i=0, j=0) == True
    
    pattern = "ba*a?"
    assert recursive_wildcard_pattern_matching2(string, pattern, i=0, j=0) == True
    
    pattern = "a*ab"
    assert recursive_wildcard_pattern_matching2(string, pattern, i=0, j=0) == False
