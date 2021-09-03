import logging
from week5.dp_text_segmentation import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_memo_splitable1():
    dictionary = {  'BOT', 'BOTH', 'THE', 'HE', 'HEAR', 'HEART', 'HEARTH', 
                    'EARTH', 'ART', 'HAND', 'HANDS', 'AND', 'SATURN', 'AT',
                    'TURN', 'TURNS', 'URN', 'URNS', 'SPIN', 'PIN'}
    S = 'BOTH'
    i = 0
    memo = dict()
    assert memo_splitable(S, i, dictionary, memo) == True
    assert dp_splitable(S, dictionary) == True
    
    S = 'BOTHEARTH'
    i = 0
    memo = dict()
    assert memo_splitable(S, i, dictionary, memo) == True
    assert dp_splitable(S, dictionary) == True
    
    S = 'BOTHEARTHE'
    i = 0
    memo = dict()
    assert memo_splitable(S, i, dictionary, memo) == True
    assert dp_splitable(S, dictionary) == True
    
    S = 'BOTHEARTHANDSATURNSPIN'
    i = 0
    memo = dict()
    assert memo_splitable(S, i, dictionary, memo) == True
    assert dp_splitable(S, dictionary) == True
    
    S = 'SATURNSPIN'
    i = 0
    memo = dict()
    assert memo_splitable(S, i, dictionary, memo) == True
    assert dp_splitable(S, dictionary) == True