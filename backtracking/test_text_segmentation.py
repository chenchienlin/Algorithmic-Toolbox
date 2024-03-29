import logging
from backtracking.text_segmentation import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_splitable1():
    dictionary = {  'BOT', 'BOTH', 'THE', 'HE', 'HEAR', 'HEART', 'HEARTH', 
                    'EARTH', 'ART', 'HAND', 'HANDS', 'AND', 'SATURN', 'AT',
                    'TURN', 'TURNS', 'URN', 'URNS', 'SPIN', 'PIN'}
    S = 'BOTH'
    i = 0
    assert splitable(S, i, dictionary) == True
    
    S = 'BOTHEARTH'
    i = 0
    assert splitable(S, i, dictionary) == True
    
    S = 'BOTHEARTHE'
    i = 0
    assert splitable(S, i, dictionary) == True
    
    S = 'BOTHEARTHANDSATURNSPIN'
    i = 0
    assert splitable(S, i, dictionary) == True
    
    S = 'SATURNSPIN'
    i = 0
    assert splitable(S, i, dictionary) == True

def test_construct_text_segmentation1():
    dictionary = {  'BOT', 'BOTH', 'THE', 'HE', 'HEAR', 'HEART', 'HEARTH', 
                    'EARTH', 'ART', 'HAND', 'HANDS', 'AND', 'SATURN', 'AT',
                    'TURN', 'TURNS', 'URN', 'URNS', 'SPIN', 'PIN'}
    S = 'BOTHEARTHANDSATURNSPIN'
    i = 0
    segs = construct_text_segmentation(S, i, dictionary)
    LOGGER.debug(segs)
    for seg in segs:
        assert seg in dictionary

def test_count_partition():
    dictionary = {  'BOT', 'BOTH', 'THE', 'HE', 'HEAR', 'HEART', 'HEARTH', 
                    'EARTH', 'ART', 'HAND', 'HANDS', 'AND', 'SATURN', 'AT',
                    'TURN', 'TURNS', 'URN', 'URNS', 'SPIN', 'PIN'}
    # 1. BOT HE ART
    # 2. BOT HEART
    S = 'BOTHEART'
    i = 0
    assert count_partition(S, i, dictionary) == 2
    
    # 1. HAND SATURN
    # 2. HANDS AT URN
    S = 'HANDSATURN'
    i = 0
    assert count_partition(S, i, dictionary) == 2

def test_construct_all_segmentations1():
    dictionary = ["cat","cats","and","sand","dog"]
    S = "catsanddog"
    i = 0
    assert construct_all_segmentations(S, i, dictionary) == ['cat sand dog', 'cats and dog']
    
    dictionary = ["cat","and","sand","dog"]
    S = "catsanddog"
    i = 0
    assert construct_all_segmentations(S, i, dictionary) == ['cat sand dog']
    
    dictionary = ["cats","and","sand","dog"]
    S = "catsanddog"
    i = 0
    assert construct_all_segmentations(S, i, dictionary) == ['cats and dog']

def test_construct_all_segmentations2():
    dictionary = ["apple","pen","applepen","pine","pineapple"]
    S = "applepenapple"
    i = 0
    assert construct_all_segmentations(S, i, dictionary) == ['apple pen apple', 'applepen apple']
    
    S = "pineapplepenapple"
    i = 0
    assert construct_all_segmentations(S, i, dictionary) == ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']

def test_construct_all_segmentations3():
    dictionary = ["cats","dog","sand","and","cat"]
    S = "catsandog"
    i = 0
    assert construct_all_segmentations(S, i, dictionary) == []