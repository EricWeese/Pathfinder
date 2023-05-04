import pygame
import sys
from queue import PriorityQueue
import Node


BLACK = (30, 30, 30)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
LIGHTBLUE = (131, 174, 242)
YELLOW = (200, 200, 0)
colorDictionary = {
    (200, 200, 200): 0,  # White cell
    (30, 30, 30): 1,  # Wall cell
    (0, 200, 0): 2,  # Start cell
    (200, 0, 0): 3,  # End cell
    (200, 200, 0): 4,  # Expanded cell
    (0, 0, 200): 5,  # Current Cell
    (131, 174, 242): 6,  # Path Cell
}
blockSize = 20  # Set the size of the grid block
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
ROWS = int(WINDOW_WIDTH / blockSize)
COLS = int(WINDOW_HEIGHT / blockSize)
TICKTIME = 1
STARTCOEF, ENDCOEF = 1, 1
pygame.font.init()
FONT = pygame.font.SysFont("monospace", 15)
grid = []  # Initializing grid
prevGrid = []
start = []
end = []


def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 0)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def clearGrid():
    global grid
    grid = []
    for x in range(0, WINDOW_WIDTH, blockSize):
        col = []
        for y in range(0, WINDOW_HEIGHT, blockSize):
            col.append(0)  # Set everything to blank space
        grid.append(col)


def resetGrid():
    i, j = 0, 0
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            c = grid[i][j]
            if c == 4 or c == 5 or c == 6:
                grid[i][j] = 0
                rect = pygame.Rect(y, x, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect, 0)
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
            j += 1
        j = 0
        i += 1


def printGrid():
    for row in grid:
        for col in row:
            print(col, end="")
        print()
    print()


def setCell(color, x, y):
    #print(f'Printing {colorDictionary[color]} at {y}, {x}')
    gridx = x
    gridy = y
    global grid
    grid[gridy][gridx] = colorDictionary[color]
    x = gridx * blockSize
    y = gridy * blockSize
    rect = pygame.Rect(x, y, blockSize, blockSize)
    pygame.draw.rect(SCREEN, color, rect, 0)
    pygame.draw.rect(SCREEN, BLACK, rect, 1)


# Checks if to make sure there is start and end point
def checkGrid():
    i, j = 0, 0
    global start, end
    startFlag = False
    endFlag = False
    for row in grid:
        for col in row:
            if grid[j][i] == 2:
                startFlag = True
                start = [j, i]
            elif grid[j][i] == 3:
                endFlag = True
                end = [j, i]
            j += 1
        j = 0
        i += 1
    if not startFlag:
        print("You need a start point")
        return False
    if not endFlag:
        print("You need an end point")
        return False
    return True


def UCS():
    if not checkGrid():  # Checks for starting and ending point
        return
    resetGrid()  # Resets the grid (gets rid of yellow and light blue cells. Keeps start, end, and wall cells)
    global FONT, TICKTIME
    completed = False  # Variable is set to true once end cell has been reached
    visited = []  # List of all visited cell's coords
    root = Node.Node(start[0], start[1], 0)  # Root of search tree
    newNode = root  # Initialize new node as root
    prevNode = root  # Initialize prev node as root
    # List of cells to be expanded. Conatins row, col, and node associated with that cell
    cellQueue = [[start[0], start[1], prevNode]]
    # Coords for previously expanded node. [-1, -1] are just default values
    prev = [-1, -1]
    prevDistance = -1
    i = 0  # Counts iterations
    while not completed:
        # Waits 10ms so user can visualize algorithm
        pygame.time.wait(TICKTIME)
        # Contains both coords and node belonging to cell
        currRaw = cellQueue.pop(0)
        curr = [currRaw[0], currRaw[1]]  # List of just the coords
        visited.append(curr)  # Appends current cell to visited list
        currRow = curr[0]  # Row number
        currCol = curr[1]  # Col number
        distance = abs(curr[1] - start[1]) + abs(curr[0] - start[0])
        # Node of the cell that allowed this cell to be searched (node.parent)
        prevNode = currRaw[2]
        if i > 0:  # Skips first iteration
            distance = prevNode.get_distance()+1
            # Creates new node with current cell coords
            newNode = Node.Node(currRow, currCol, distance)
            # Makes this cell a child of the previous cell
            prevNode.add_child(newNode)
        if i > 1:  # Skips first and second iteration
            # Color the current cell blue (only ever one cell)
            setCell(BLUE, curr[1], curr[0])
            # Color the previous cell yellow (all exapanded cells are yellow)
            setCell(YELLOW, prev[1], prev[0])
            distanceText = FONT.render(str(prevDistance), False, (0, 0, 0))
            if prevDistance < 10:
                SCREEN.blit(
                    distanceText, (prev[1]*blockSize+5, prev[0]*blockSize+1))
            else:
                SCREEN.blit(
                    distanceText, (prev[1]*blockSize+1, prev[0]*blockSize+1))

        prevDistance = distance
        # Sets the previous cell to the current cell
        prev[0], prev[1] = curr[0], curr[1]
        right, up, left, down = [currRow, currCol+1], [currRow +
                                                       1, currCol], [currRow, currCol-1], [currRow-1, currCol]  # Shorthand variable for right, up, left, and down cell
        # List of just cell coords (excludes nodes). Used to determine if cell is already in queue.
        cellQueueCut = [[x[0], x[1]] for x in cellQueue]
        """
        Given the current cell, we check all surrounding cells. If the surrounding cell is within the limits of the screen,
        not a wall, not already expanded, and not already in the cell queue then we add it to the cell queue. We add the 
        cell's row, col, and the node the was initialized above all as one list.
        """
        # Right cell
        if currCol < WINDOW_WIDTH//blockSize-1 and right not in visited and right not in cellQueueCut and grid[currRow][currCol+1] != 1:
            cellQueue.append([currRow, currCol+1, newNode])
        # Up Cell
        if currRow < WINDOW_HEIGHT//blockSize-1 and up not in visited and up not in cellQueueCut and grid[currRow+1][currCol] != 1:
            cellQueue.append([currRow+1, currCol, newNode])
        # Left Cell
        if currCol > 0 and left not in visited and left not in cellQueueCut and grid[currRow][currCol-1] != 1:
            cellQueue.append([currRow, currCol-1, newNode])
        # Down Cell
        if currRow > 0 and down not in visited and down not in cellQueueCut and grid[currRow-1][currCol] != 1:
            cellQueue.append([currRow-1, currCol, newNode])

        if curr == end:  # Checks to see if the end node has been reached
            # Completed is now true which will trigger while loop to stop.
            completed = True
            # Following code makes light blue path
            pathCell = newNode.get_data()  # Gets the end node coords
            setCell(RED, pathCell[1], pathCell[0])  # Sets end node back to red
            newNode = newNode.get_parent()  # Gets the node on which this node was expanded from
            pathLength = 0
            while newNode.get_parent() != None:  # Keeps going to all the nodes parents until back at start node
                pygame.time.wait(TICKTIME)
                pathCell = newNode.get_data()  # Gets nodes coords
                # Sets the current cell to lightblue
                setCell(LIGHTBLUE, pathCell[1], pathCell[0])
                distanceText = FONT.render(
                    str(newNode.get_distance()), False, (0, 0, 0))
                if newNode.get_distance() < 10:
                    SCREEN.blit(
                        distanceText, (pathCell[1]*blockSize+5, pathCell[0]*blockSize+1))
                else:
                    SCREEN.blit(
                        distanceText, (pathCell[1]*blockSize+1, pathCell[0]*blockSize+1))
                newNode = newNode.get_parent()  # Gets the parent node
                pathLength += 1
                pygame.display.update()
            print("UCS")
            print(f"Path Length: {pathLength+1}")
            print(f"Nodes Expanded: {i-1}\n")
            break
        i += 1
        pygame.display.update()  # Updates the screen every iteration


def Hueristic(f):
    if not checkGrid():  # Checks for starting and ending point
        return
    resetGrid()  # Resets the grid (gets rid of yellow and light blue cells. Keeps start, end, and wall cells)
    global FONT, TICKTIME
    completed = False  # Variable is set to true once end cell has been reached
    visited = []  # List of all visited cell's coords
    root = Node.Node(start[0], start[1], 0)  # Root of search tree
    newNode = root  # Initialize new node as root
    prevNode = root  # Initialize prev node as root
    #cellQueue = PriorityQueue()
    cellQueue = []
    cellQueue.append([0, start[0], start[1], prevNode])
    prev = [-1, -1]
    prevDistance = -1
    i = 0
    # Start and End hueristic coefficient (lower end -> UCS(1,0), lower start -> BFS(0,1))
    global STARTCOEF, ENDCOEF
    while not completed:
        pygame.time.wait(TICKTIME)
        cellQueue.sort(reverse=False)
        currRaw = cellQueue.pop(0)
        curr = [currRaw[1], currRaw[2]]  # List of just the coords
        visited.append(curr)
        currRow = curr[0]
        currCol = curr[1]
        if f == "bfs":
            distanceFromEnd = abs(curr[0] - end[0]) + abs(curr[1] - end[1])
        elif f == "a*":
            distanceFromStart = 1

        # Node of the cell that allowed this cell to be searched (node.parent)
        prevNode = currRaw[3]
        if i > 0:  # Skips first iteration
            distanceFromStart = prevNode.get_distance()+1
            distanceFromEnd = abs(curr[0] - end[0]) + abs(curr[1] - end[1])
            # Creates new node with current cell coords
            newNode = Node.Node(currRow, currCol, distanceFromStart)
            # Makes this cell a child of the previous cell
            prevNode.add_child(newNode)
        if i > 1:  # Skips first and second iteration
            # Color the current cell blue (only ever one cell)
            setCell(BLUE, curr[1], curr[0])
            # Color the previous cell yellow (all exapanded cells are yellow)
            setCell(YELLOW, prev[1], prev[0])
            distanceText = FONT.render(
                str(int(prevDistance)), False, (0, 0, 0))
            if prevDistance < 10:
                SCREEN.blit(
                    distanceText, (prev[1]*blockSize+5, prev[0]*blockSize+1))
            else:
                SCREEN.blit(
                    distanceText, (prev[1]*blockSize+1, prev[0]*blockSize+1))

        if f == "bfs":
            prevDistance = distanceFromEnd
        elif f == "a*":
            distanceEnd = abs(curr[0] - end[0]) + abs(curr[1] - end[1])
            prevDistance = (STARTCOEF*distanceFromStart) + \
                (ENDCOEF*distanceEnd)
        # Sets the previous cell to the current cell
        prev[0], prev[1] = curr[0], curr[1]
        right, down, left, up = [currRow, currCol+1], [currRow +
                                                       1, currCol], [currRow, currCol-1], [currRow-1, currCol]  # Shorthand variable for right, up, left, and down cell
        # List of just cell coords (excludes nodes). Used to determine if cell is already in queue.
        cellQueueCut = [[x[1], x[2]] for x in cellQueue]
        # Right cell
        if currCol < WINDOW_WIDTH//blockSize-1 and right not in visited and right not in cellQueueCut and grid[currRow][currCol+1] != 1:
            if f == "bfs":
                distanceTemp = abs(right[0] - end[0]) + abs(right[1] - end[1])
            elif f == "a*":
                distanceEnd = abs(right[0] - end[0]) + abs(right[1] - end[1])
                distanceTemp = (STARTCOEF*distanceFromStart) + \
                    (ENDCOEF*distanceEnd)
            cellQueue.append([distanceTemp, currRow, currCol+1, newNode])
        # Down Cell
        if currRow < WINDOW_HEIGHT//blockSize-1 and down not in visited and down not in cellQueueCut and grid[currRow+1][currCol] != 1:
            if f == "bfs":
                distanceTemp = abs(down[0] - end[0]) + abs(down[1] - end[1])
            elif f == "a*":
                distanceEnd = abs(down[0] - end[0]) + abs(down[1] - end[1])
                distanceTemp = (STARTCOEF*distanceFromStart) + \
                    (ENDCOEF*distanceEnd)
            cellQueue.append([distanceTemp, currRow+1, currCol, newNode])
        # Left Cell
        if currCol > 0 and left not in visited and left not in cellQueueCut and grid[currRow][currCol-1] != 1:
            if f == "bfs":
                distanceTemp = abs(left[0] - end[0]) + abs(left[1] - end[1])
            elif f == "a*":
                distanceEnd = abs(left[0] - end[0]) + abs(left[1] - end[1])
                distanceTemp = (STARTCOEF*distanceFromStart) + \
                    (ENDCOEF*distanceEnd)
            cellQueue.append([distanceTemp, currRow, currCol-1, newNode])
        # Up Cell
        if currRow > 0 and up not in visited and up not in cellQueueCut and grid[currRow-1][currCol] != 1:
            if f == "bfs":
                distanceTemp = abs(up[0] - end[0]) + abs(up[1] - end[1])
            elif f == "a*":
                distanceEnd = abs(up[0] - end[0]) + abs(up[1] - end[1])
                distanceTemp = (STARTCOEF*distanceFromStart) + \
                    (ENDCOEF*distanceEnd)
            cellQueue.append([distanceTemp, currRow-1, currCol, newNode])
        if curr == end:  # Checks to see if the end node has been reached
            # Completed is now true which will trigger while loop to stop.
            completed = True
            # Following code makes light blue path
            pathCell = newNode.get_data()  # Gets the end node coords
            setCell(RED, pathCell[1], pathCell[0])  # Sets end node back to red
            newNode = newNode.get_parent()  # Gets the node on which this node was expanded from
            pathLength = 0
            while newNode.get_parent() != None:  # Keeps going to all the nodes parents until back at start node
                pygame.time.wait(TICKTIME)
                pathCell = newNode.get_data()  # Gets nodes coords
                # Sets the current cell to lightblue
                setCell(LIGHTBLUE, pathCell[1], pathCell[0])
                distanceText = FONT.render(
                    str(int(newNode.get_distance())), False, (0, 0, 0))
                if newNode.get_distance() < 10:
                    SCREEN.blit(
                        distanceText, (pathCell[1]*blockSize+5, pathCell[0]*blockSize+1))
                else:
                    SCREEN.blit(
                        distanceText, (pathCell[1]*blockSize+1, pathCell[0]*blockSize+1))
                newNode = newNode.get_parent()  # Gets the parent node
                pathLength += 1
                pygame.display.update()
            print(f.upper())
            print(f"Path Length: {pathLength+1}")
            print(f"Nodes Expanded: {i-1}\n")
            break

        i += 1
        pygame.display.update()


def AStar():
    Hueristic("a*")


def BFS():
    Hueristic("bfs")


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
            if pygame.mouse.get_pressed()[0]:  # Create cell (LMB)
                x, y = pygame.mouse.get_pos()
                if not start:  # Create starting cell (first click)
                    setCell(GREEN, x // blockSize, y // blockSize)
                    start = True
                elif not end:  # Create ending cell (second click)
                    setCell(RED, x // blockSize, y // blockSize)
                    end = True
                else:  # Create wall (all remaining clicks)
                    setCell(BLACK, x // blockSize, y // blockSize)
            if pygame.mouse.get_pressed()[1]:  # Testing (Middle Mouse button)
                x, y = pygame.mouse.get_pos()
                setCell(RED, x // blockSize, y // blockSize)
            if pygame.mouse.get_pressed()[2]:  # Delete cell (RMB)
                x, y = pygame.mouse.get_pos()
                setCell(WHITE, x // blockSize, y // blockSize)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    UCS()
                elif event.key == pygame.K_n:
                    BFS()
                elif event.key == pygame.K_m:
                    AStar()
                elif event.key == pygame.K_r:
                    start, end = False, False
                    drawGrid()
                    clearGrid()
                elif event.key == pygame.K_DELETE:
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
