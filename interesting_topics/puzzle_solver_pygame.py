import sys
import pygame

N_COL = 4
N_ROW = 4
BLOCK_SIZE = 100
WINDOW_WIDTH = BLOCK_SIZE * N_COL
WINDOW_HEIGHT = BLOCK_SIZE * N_ROW

BLOCK = (134, 84, 57) #865439
BACKGROUND = (215, 177, 157) #D7B19D
NUMBER = (251, 232, 211) #FBE8D3

SCREEN = None


def draw_board():
    global BLOCK_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN
    FONT = pygame.font.SysFont('Arial', 25)
    if SCREEN is not None:
        N = 1
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                if N < 16:
                    pygame.draw.rect(SCREEN, BLOCK, rect, 0)
                    tmp = FONT.render(str(N), True, NUMBER)
                    SCREEN.blit(tmp, tmp.get_rect(center=rect.center))
                # else:
                    # pygame.draw.rect(SCREEN, BLOCK, rect, 0)
                N += 1
        for i in range(0, 4+1):
            pygame.draw.line(SCREEN, BACKGROUND, (0, i*BLOCK_SIZE), (4*BLOCK_SIZE, i*BLOCK_SIZE), 5)
            pygame.draw.line(SCREEN, BACKGROUND, (i*BLOCK_SIZE, 0), (i*BLOCK_SIZE, 4*BLOCK_SIZE), 5)

def main():
    global SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BACKGROUND)
    draw_board()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()