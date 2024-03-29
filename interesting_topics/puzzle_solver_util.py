import math
from random import randint
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def find_idx(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

def idx_to_xy(idx, n_col=4):
    # index               coordinate
    # [ 0  1  2  3]       [(0,0) (0,1) (0,2) (0,3)]
    # [ 4  5  6  7]       [(1,0) (1,1) (1,2) (1,3)]
    # [ 8  9 10 11]       [(2,0) (2,1) (2,2) (2,3)]
    # [12 13 14 15]       [(3,0) (3,1) (3,2) (3,3)] 
    
    y = math.floor(idx/n_col)
    x = idx - y * n_col
    return x, y

def xy_to_idx(x, y, n_col=4):
    return x + y * n_col

def find_ngbrs(idx, n_col=4, n_row=4):
    x, y = idx_to_xy(idx)
    N_NGBRS = 4
    ngbrs = [None for _ in range(N_NGBRS)]
    # left
    if x-1 >= 0:
        ngbrs[0] = xy_to_idx(x-1, y)
    # top
    if y-1 >= 0:
        ngbrs[1] = xy_to_idx(x, y-1)
    # right 
    if x+1 < n_col:
        ngbrs[2] = xy_to_idx(x+1, y)
    # down
    if y+1 < n_row:
        ngbrs[3] = xy_to_idx(x, y+1)
    return ngbrs

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def print_puzzle(puzzle, n_col=4, n_row=4):
    s = '\n'
    for r in range(n_row):
        for c in range(n_col):
            idx = xy_to_idx(c, r)
            n_digit = len(str((puzzle[idx])))
            if n_digit == 1:
                s = f'{s} {puzzle[idx]} '
            else:
                s = f'{s} {puzzle[idx]}'
        s = f'{s}\n'
    LOGGER.debug(s)

def compute_successors(predecessor, blank_idx=None, initial=None):
    BLANK = 16
    if blank_idx == None:
        blank_idx = find_idx(predecessor, BLANK)
    ngbrs = find_ngbrs(blank_idx)
    successors = []
    for nb in ngbrs:
        if nb is not None:
            puzzle = predecessor.copy()
            swap(puzzle, blank_idx, nb)
            if initial is None:
                successors.append(puzzle)
            elif initial is not None and puzzle != initial:
                successors.append(puzzle)
    return successors

def list_to_str(l):
    return " ".join(str(elem) for elem in l)

def generate_puzzle(max_degree):
    size = 16
    puzzle = [i+1 for i in range(size)]
    for _ in range(max_degree):
        successors = compute_successors(puzzle)
        rand = randint(0, len(successors)-1)
        puzzle = successors[rand]
    return puzzle

def find_swap(state1, state2):
    BLANK = 16
    move = [i for i in range(len(state1)) if state1[i] != state2[i]]
    
    # Let the blank block be the first item in move
    if state1[move[1]] == BLANK:
        swap(move,0,1)
    return move