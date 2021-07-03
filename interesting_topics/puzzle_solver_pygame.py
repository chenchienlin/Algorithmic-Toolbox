import sys
import pygame
from interesting_topics.puzzle_solver_util import idx_to_xy, swap, find_idx
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

N_COL = 4
N_ROW = 4
BLOCK_SIZE = 100
WINDOW_WIDTH = BLOCK_SIZE * N_COL
WINDOW_HEIGHT = BLOCK_SIZE * N_ROW

BLOCK = (134, 84, 57) #865439
BACKGROUND = (215, 177, 157) #D7B19D
NUMBER = (251, 232, 211) #FBE8D3
FONT = None
SCREEN = None

# Custom Event
solve_event = pygame.USEREVENT + 1
SOLVE_EVENT_TIME = 10

def draw_board(initial):
    global BLOCK_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN, FONT
    FONT = pygame.font.SysFont('Arial', 25)
    if SCREEN is not None:
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
                N = initial.pop(0)
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                if N < 16:
                    pygame.draw.rect(SCREEN, BLOCK, rect, 0)
                    tmp = FONT.render(str(N), True, NUMBER)
                    SCREEN.blit(tmp, tmp.get_rect(center=rect.center))
                else:
                    pygame.draw.rect(SCREEN, BACKGROUND, rect, 0)
        
        for i in range(0, 4+1):
            pygame.draw.line(SCREEN, BACKGROUND, (0, i*BLOCK_SIZE), (4*BLOCK_SIZE, i*BLOCK_SIZE), 5)
            pygame.draw.line(SCREEN, BACKGROUND, (i*BLOCK_SIZE, 0), (i*BLOCK_SIZE, 4*BLOCK_SIZE), 5)

def update_board(x, y, N):
    global BLOCK_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN, FONT
    x = x * BLOCK_SIZE
    y = y * BLOCK_SIZE
    rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
    if N < 16:
        pygame.draw.rect(SCREEN, BLOCK, rect, 0)
        tmp = FONT.render(str(N), True, NUMBER)
        SCREEN.blit(tmp, tmp.get_rect(center=rect.center))
    else:
        pygame.draw.rect(SCREEN, BACKGROUND, rect, 0)
    
    for i in range(0, 4+1):
        pygame.draw.line(SCREEN, BACKGROUND, (0, i*BLOCK_SIZE), (4*BLOCK_SIZE, i*BLOCK_SIZE), 5)
        pygame.draw.line(SCREEN, BACKGROUND, (i*BLOCK_SIZE, 0), (i*BLOCK_SIZE, 4*BLOCK_SIZE), 5)

def main(initial, moves=None):
    global SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BACKGROUND)
    draw_board(initial.copy())
    
    finished = False    
    moves_iter = iter(moves)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # set custom event
                    pygame.time.set_timer(solve_event, SOLVE_EVENT_TIME)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == solve_event and finished is False:
                m = next(moves_iter, None)
                if m is None:
                    finished = True
                else:
                    blank_idx = m[0]
                    ngbr_idx = m[1]
                    LOGGER.debug(f'blank_idx : {blank_idx}')
                    LOGGER.debug(f'ngbr_idx : {ngbr_idx}')
                    
                    blank_x, blank_y = idx_to_xy(blank_idx)
                    ngbr_x, ngbr_y = idx_to_xy(ngbr_idx)
                    
                    LOGGER.debug(f'blank_x blank_y: {blank_x} {blank_y}')
                    LOGGER.debug(f'ngbr_x ngbr_y: {ngbr_x} {ngbr_y}')
                    
                    blank_v = initial[blank_idx]
                    ngbr_v = initial[ngbr_idx]
                    
                    LOGGER.debug(f'blank_v : {blank_v}')
                    LOGGER.debug(f'ngbr_v : {ngbr_v}')
                    
                    update_board(blank_x, blank_y, ngbr_v)
                    update_board(ngbr_x, ngbr_y, blank_v)
                    swap(initial, m[0], m[1])
                    
        pygame.display.update()

if __name__ == '__main__':
    main()