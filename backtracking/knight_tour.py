from math import floor
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def xy_to_idx(x, y, n_col=8):
    return x + y * n_col

def knight_moves():
    mx = [-2,-1,1,2]
    my = [-2,-1,1,2]
    moves = []
    for xi in mx:
        for yi in my:
            if abs(xi) + abs(yi) == 3:
                moves.append([xi, yi])
    return moves
    
def knight_tour(x, y, M, MOVES, i=1):
    if i ==64:
        return True
    else:
        for m in MOVES:
            new_x, new_y = x + m[0], y + m[1]
            if new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8 and M[new_x][new_y] == -1:
                M[new_x][new_y] = i
                result = knight_tour(new_x, new_y, M, MOVES, i+1)
                if result == True:
                    return True
                M[new_x][new_y] == -1
        return False