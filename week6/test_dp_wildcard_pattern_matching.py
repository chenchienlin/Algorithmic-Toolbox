import logging
from week6.dp_wildcard_pattern_matching import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_dp_wildcard_pattern_matching1():
    pattern = '?arl'
    string = 'Karl'
    assert dp_wildcard_pattern_matching(string, pattern) == True
    
    string = 'Kurl'
    assert dp_wildcard_pattern_matching(string, pattern) == False
    
    string = 'Carl'
    assert dp_wildcard_pattern_matching(string, pattern) == True
    
    string = 'Kur'
    assert dp_wildcard_pattern_matching(string, pattern) == False
    
    string = 'Karll'
    assert dp_wildcard_pattern_matching(string, pattern) == False
    
    string = ''
    assert dp_wildcard_pattern_matching(string, pattern) == False

def test_dp_wildcard_pattern_matching2():
    string = "baaabab"
    
    pattern = "*****ba*****ab"
    assert dp_wildcard_pattern_matching(string, pattern) == True
    
    pattern = "baaa?ab"
    assert dp_wildcard_pattern_matching(string, pattern) == True
    
    pattern = "ba*a?"
    assert dp_wildcard_pattern_matching(string, pattern) == True
    
    pattern = "a*ab"
    assert dp_wildcard_pattern_matching(string, pattern) == False
