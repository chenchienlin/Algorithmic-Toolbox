import logging
from week3.stable_matching import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_perference1():
    # preference list of hospitals
    hospitals = [
        [3,2,1,0], # A hospital
        [1,3,0,2], # B hospital
        [3,1,2,0], # C hospital
        [2,1,0,3]] # D hospital
    
    # preference list of interns
    interns = [
        [0,1,2,3],
        [0,3,2,1],
        [1,0,2,3],
        [3,1,2,0]]
    
    assert preference(interns, 0, 0) == 0
    assert preference(interns, 0, 1) == 1
    assert preference(interns, 0, 2) == 2
    assert preference(interns, 0, 3) == 3
    
    assert preference(interns, 1, 0) == 0
    assert preference(interns, 1, 1) == 3
    assert preference(interns, 1, 2) == 2
    assert preference(interns, 1, 3) == 1
    
    assert preference(interns, 2, 0) == 1
    assert preference(interns, 2, 1) == 0
    assert preference(interns, 2, 2) == 2
    assert preference(interns, 2, 3) == 3
    
    assert preference(interns, 3, 0) == 3
    assert preference(interns, 3, 1) == 1
    assert preference(interns, 3, 2) == 2
    assert preference(interns, 3, 3) == 0

def test_stable_matching():
    # preference list of hospitals
    hospitals = [
        [3,2,1,0], # A hospital
        [1,3,0,2], # B hospital
        [3,1,2,0], # C hospital
        [2,1,0,3]] # D hospital
    
    # preference list of interns
    interns = [
        [0,1,2,3],
        [0,3,2,1],
        [1,0,2,3],
        [3,1,2,0]]
    
    _, _, records = stable_matching(interns, hospitals)
    assert records[0] == [3, None, None, None]
    assert records[1] == [3, 1, None, None]
    assert records[2] == [None, 1, 3, None]
    assert records[3] == [None, 1, 3, 2]
    assert records[4] == [2, 1, 3, None]
    assert records[5] == [2, None, 3, 1]
    assert records[6] == [2, 3, None, 1]
    assert records[7] == [2, 3, None, 1]
    assert records[8] == [2, 3, None, 1]
    assert records[9] == [2, 3, 0, 1]