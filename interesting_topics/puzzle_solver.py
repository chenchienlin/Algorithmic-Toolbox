from collections import deque
from interesting_topics.puzzle_solver_util import *
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def BFSSolver(initial, goal):
    BLANK = 16
    Q = deque()
    Q.append(initial)
    prev = dict()
    prev[list_to_str(initial)] = None
    state = None
    while True:
        state = Q.popleft()
        if state == goal:
            # return prev
            break
        successors = compute_successors(state, initial=initial)
        for suc in successors:
            if list_to_str(suc) not in prev:
                prev[list_to_str(suc)] = state
                Q.append(suc)
    curr = state
    record = []
    while curr:
        record.append(curr)
        curr = prev[list_to_str(curr)]
    
    moves = []
    curr = record.pop()
    while curr != goal:
        print_puzzle(curr)
        next = record.pop()
        motion = find_swap(curr, next)
        moves.append(motion)
        LOGGER.debug(f'Swap {curr[motion[0]]} {curr[motion[1]]}\n')
        curr = next
    print_puzzle(curr)
    return curr, moves