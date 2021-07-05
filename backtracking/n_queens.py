def detect_attack(prev_row, prev_col, curr_row):
    diff = curr_row - prev_row
    return [prev_col-diff, prev_col, prev_col+diff]

def detect_all_attack(Q, curr_row):
    all_invalid = []
    for prev_row in range(curr_row): # prev_row=0:curr_row-1
        prev_col = Q[prev_row]
        invalid = detect_attack(prev_row, prev_col, curr_row)
        for i in invalid:
            if i > 0 or i <= len(Q)-1:
                all_invalid.append(i)
    return all_invalid

prev_row = 0
prev_col = 4
curr_row = 1
invalid = detect_attack(prev_row, prev_col, curr_row)
print(invalid)

curr_row = 2
invalid = detect_attack(prev_row, prev_col, curr_row)
print(invalid)


Q = [0 for _ in range(4)]
Q[0] = 1
Q[1] = 3
curr_row = 2
all_invalid = detect_all_attack(Q, curr_row)
print(all_invalid)