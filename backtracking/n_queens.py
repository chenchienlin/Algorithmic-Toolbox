import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def detect_attack(prev_row, prev_col, curr_row):
    diff = curr_row - prev_row
    return [prev_col-diff, prev_col, prev_col+diff]

def detect_all_attack(Q, curr_row):
    all_invalid = set()
    for prev_row in range(curr_row): # prev_row=0:curr_row-1
        prev_col = Q[prev_row]
        invalid = detect_attack(prev_row, prev_col, curr_row)
        all_invalid.update(invalid)
    return list(all_invalid)

def n_queens(Q, curr_row, ans):
    if curr_row >= len(Q):
        ans.append(Q.copy())
        LOGGER.debug(Q)
    all_invalid = detect_all_attack(Q, curr_row)
    for col in range(len(Q)): # col=0:len(Q)-1
        if col not in all_invalid:
            Q[curr_row] = col
            n_queens(Q, curr_row+1, ans)