import logging
from backtracking.n_queens import *
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def test_detect_attack():
    prev_row = 0
    prev_col = 4
    curr_row = 1
    invalid = detect_attack(prev_row, prev_col, curr_row)
    assert 3 in invalid
    assert 4 in invalid
    assert 5 in invalid
    
    curr_row = 2
    invalid = detect_attack(prev_row, prev_col, curr_row)
    assert 2 in invalid
    assert 4 in invalid
    assert 6 in invalid

def test_detect_all_attack1():
    #   0   1   2   3  
    # -----------------
    # |   | Q |   |   |
    # -----------------
    # |   |   |   | Q |
    # -----------------
    # |   | X | X | X |
    # -----------------
    # |   |   |   |   |
    # -----------------
    
    Q = [0 for _ in range(4)]
    Q[0] = 1
    Q[1] = 3
    curr_row = 2
    all_invalid = detect_all_attack(Q, curr_row)
    assert 1 in all_invalid
    assert 2 in all_invalid
    assert 3 in all_invalid

def test_detect_all_attack2():
    #   0   1   2   3  
    # -----------------
    # |   | Q |   |   |
    # -----------------
    # |   |   |   | Q |
    # -----------------
    # | Q |   |   |   |
    # -----------------
    # | X | X |   | X |
    # -----------------
    
    Q = [0 for _ in range(4)]
    Q[0] = 1
    Q[1] = 3
    Q[2] = 0
    curr_row = 3
    all_invalid = detect_all_attack(Q, curr_row)
    assert 0 in all_invalid
    assert 1 in all_invalid
    assert 3 in all_invalid

def test_n_queens1():
    #   0   1   2   3      0   1   2   3  
    # -----------------  -----------------
    # |   | Q |   |   |  |   |   | Q |   |
    # -----------------  -----------------
    # |   |   |   | Q |  | Q |   |   |   |
    # -----------------  -----------------
    # | Q |   |   |   |  |   |   |   | Q |
    # -----------------  -----------------
    # |   |   | Q |   |  |   | Q |   |   |
    # -----------------  -----------------
    ans = []
    Q = [0 for i in range(4)]
    curr_row = 0
    n_queens(Q, curr_row, ans)
    assert [1,3,0,2] in ans
    assert [2,0,3,1] in ans

def test_n_queens2():
    ans = []
    Q = [0 for i in range(8)]
    curr_row = 0
    n_queens(Q, curr_row, ans)
    assert len(ans) == 92