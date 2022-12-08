import pygame
import sys

BLACK = (30, 30, 30)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)
colorDictionary = {
    (200, 200, 200): 0,
    (30, 30, 30): 1,
    (0, 200, 0): 2,
    (200, 0, 0): 3,
}
blockSize = 20 #Set the size of the grid block
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
ROWS = int(WINDOW_WIDTH / blockSize)
COLS = int(WINDOW_HEIGHT / blockSize)

grid = [] #Initializing grid


def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def clearGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        col = []
        for y in range(0, WINDOW_HEIGHT, blockSize):
            col.append(0)  # Set everything to blank space
        grid.append(col)

def printGrid():
    i = 0
    j = 0
    for row in grid:
        for col in row:
            print(col, end="")
            j += 1
        i += 1
        print()

def setCell(color):
    x, y = pygame.mouse.get_pos()
    gridx = (x // blockSize)
    gridy = (y // blockSize)
    grid[gridy][gridx] = colorDictionary[color]
    printGrid()
    x = gridx * blockSize
    y = gridy * blockSize
    rect = pygame.Rect(x, y, blockSize, blockSize)
    if color == WHITE:
        pygame.draw.rect(SCREEN, WHITE, rect, 0)
        pygame.draw.rect(SCREEN, BLACK, rect, 1)
    else:
        pygame.draw.rect(SCREEN, color, rect, 0)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    start, end = False, False
    clearGrid()

    drawGrid()
    while True:
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                if not start:
                    setCell(GREEN)
                    start = True
                elif not end:
                    setCell(RED)
                    end = True
                else:
                    setCell(BLACK)
            if pygame.mouse.get_pressed()[2]:
                setCell(WHITE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #getNode()
                pass
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()