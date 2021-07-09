from math import floor

def xy_to_idx(x, y, n_col=8):
    return x + y * n_col

def knight_moves(x, y, M, n_row=8, n_col=8):
    mx = [-2,-1,1,2]
    my = [-2,-1,1,2]
    moves = []
    for xi in mx:
        for yi in my:
            if abs(xi) + abs(yi) == 3:
                moves.append([xi, yi])
    legal = []
    for m in moves:
        new_x = x + m[0]
        new_y = y + m[1]
        if new_x >= 0 and new_y >= 0 and new_x < n_col and new_y < n_row:
            idx = xy_to_idx(new_x, new_y)
            if idx not in M:
                legal.append([new_x, new_y])
    return legal

def knight_tour(x, y, M, i=1):
    if i ==64:
        return True
    else:
        valid_moves = knight_moves(x, y, M)
        best = False
        for m in valid_moves:
            new_x, new_y = m[0], m[1]
            M[i] = xy_to_idx(new_x, new_y)
            print(M)
            result = knight_tour(new_x, new_y, M, i+1)
            if result == False:
                M[i] = -1
            print(result)
            if result == True:
                best = True
        return best