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


def test_dp_splitable21():
    dictionary = ["cat","cats","and","sand","dog"]
    S = "catsanddog"
    i = 0
    assert dp_splitable2(S, dictionary) == ['cat sand dog', 'cats and dog']
    
    dictionary = ["cat","and","sand","dog"]
    S = "catsanddog"
    i = 0
    assert dp_splitable2(S, dictionary) == ['cat sand dog']
    
    dictionary = ["cats","and","sand","dog"]
    S = "catsanddog"
    i = 0
    assert dp_splitable2(S, dictionary) == ['cats and dog']

def test_dp_splitable22():
    dictionary = ["apple","pen","applepen","pine","pineapple"]
    S = "applepenapple"
    i = 0
    assert dp_splitable2(S, dictionary) == ['apple pen apple', 'applepen apple']
    
    S = "pineapplepenapple"
    i = 0
    assert dp_splitable2(S, dictionary) == ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']

def test_dp_splitable23():
    dictionary = ["cats","dog","sand","and","cat"]
    S = "catsandog"
    i = 0
    assert dp_splitable2(S, dictionary) == []