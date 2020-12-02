import pygame, sys
from board import Board
from cell import Cell

pygame.init()
RUN = True

# Window size
MULTIPLIER = 10  # Modify this value to change the window size
WINDOWSIZE = 81
WINDOWWIDTH = WINDOWSIZE * MULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * MULTIPLIER


# Squaresize is a grouping of cells, while each cell shows 1 number.
SQUARESIZE = int((WINDOWSIZE * MULTIPLIER) / 3)
CELLSIZE =  int(SQUARESIZE / 3)  # Size of a cell
NUMBERSIZE = int(CELLSIZE / 3)   # Position of the number

# Clock to control screen update speed
clock = pygame.time.Clock()

# A window needs a board to work with
file_name = 'easy2.txt'
game_board = Board(file_name)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGRAY = (200, 200, 200)

# Fonts
font1 = pygame.font.SysFont("comicsans", 40) 
font2 = pygame.font.SysFont("comicsans", 20) 

# Draw the cells for the sudoku grid
def draw_cells(game_board):    
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, BLACK, (i*CELLSIZE, j*CELLSIZE, CELLSIZE, CELLSIZE), 1)
            value = game_board.get_value(j, i)
            if value == 0:
                continue
            else:
                text = font1.render(str(game_board.get_value(i, j)), 1, BLACK)
                screen.blit(text, (i*CELLSIZE + NUMBERSIZE, j*CELLSIZE + NUMBERSIZE))
                

    return None

def draw_lines():
    ### Draw Major Lines
    for x in range(0, int(WINDOWWIDTH), int(SQUARESIZE)): # draw vertical lines
        pygame.draw.line(screen, BLACK, (x,0),(x,WINDOWHEIGHT), 5)
    for y in range (0, int(WINDOWHEIGHT), int(SQUARESIZE)): # draw horizontal lines
        pygame.draw.line(screen, BLACK, (0,y), (WINDOWWIDTH, y), 5)
    
    return None


if __name__ == "__main__":
    #create the screen window
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) 
    #set the screen title
    pygame.display.set_caption('Sudoku') 

    # Main game loop
    while RUN:
        #Main event loop
        for event in pygame.event.get():    #user did something
            if event.type == pygame.QUIT:  #if user clicks close
                RUN = False
        
            
        pygame.display.update()
    
    # Game logic should go here
        #do something


    # Code to draw the screen should go here
        screen.fill(WHITE)
        draw_lines()
        draw_cells(game_board)

        # Refreshes the screen
        pygame.display.flip()

        # Limit to 30 FPS
        clock.tick(30)



    pygame.quit()
    sys.exit