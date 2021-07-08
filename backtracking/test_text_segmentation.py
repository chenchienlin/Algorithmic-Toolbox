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

def test_construct_text_segmentation():
    dictionary = {  'BOT', 'BOTH', 'THE', 'HE', 'HEAR', 'HEART', 'HEARTH', 
                    'EARTH', 'ART', 'HAND', 'HANDS', 'AND', 'SATURN', 'AT',
                    'TURN', 'TURNS', 'URN', 'URNS', 'SPIN', 'PIN'}
    S = 'BOTHEARTHANDSATURNSPIN'
    i = 0
    segs = construct_text_segmentation(S, i, dictionary)
    LOGGER.debug(segs)
    for seg in segs:
        assert seg in dictionary