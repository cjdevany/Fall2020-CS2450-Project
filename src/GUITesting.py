# Initial credit: https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/
import pygame
import math


# TODO: Change colors as wanted

# Styling Options
CELL_PADDING = 3
SELECTED_CELL_THICKNESS = 5
CELL_THICKNESS = 1
BORDER_THICKNESS = 8
VALUE_PADDING = 15

# Get the height and width of the current display
pygame.display.init()
display_info = pygame.display.Info()

# Introduce a scaling factor to adjust window size
SCALING_FACTOR = 0.5

# Define window screen height and width
SCREEN_HEIGHT = math.floor(SCALING_FACTOR * display_info.current_h)
SCREEN_WIDTH = math.floor(SCALING_FACTOR * display_info.current_w)

# Create a screen with the set dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Window Name
pygame.display.set_caption("Sudoku Board Test")
# Icon options
# img = pygame.image.load('icon.png')
# pygame.display.set_icon(img)

# Fonts
pygame.font.init()
font1 = pygame.font.SysFont('comicsans', 40)
font2 = pygame.font.SysFont('comicsans', 20)

row = 0
col = 0
cell_width = SCREEN_WIDTH / 9
val = 0

test_display_grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0], 
    [6, 0, 0, 0, 7, 5, 0, 0, 9], 
    [0, 0, 0, 6, 0, 1, 0, 7, 8], 
    [0, 0, 7, 0, 4, 0, 2, 6, 0], 
    [0, 0, 1, 0, 5, 0, 9, 3, 0], 
    [9, 0, 4, 0, 6, 0, 0, 0, 5], 
    [0, 7, 0, 3, 0, 0, 0, 1, 2], 
    [1, 2, 0, 0, 0, 7, 4, 0, 0], 
    [0, 4, 9, 2, 0, 6, 0, 0, 7] 
                    ]

def get_cell(pos):
    """
    get_cell(pos): Gets the current cell based on a position array
    pos[0] contains the x-position,
    pos[1] contains the y-position.
    """
    global row, col
    row = pos[0] // cell_width
    col = pos[1] // cell_width


def draw_cell():
    """
    draw_cell(): Highlights the selected cell
    """
    # Loop used to draw side walls and top/bottom walls
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 0), (row * cell_width - CELL_PADDING, (col + i) * cell_width),
        (row * cell_width + cell_width + CELL_PADDING, (row + i) * cell_width, col * cell_width + cell_width), SELECTED_CELL_THICKNESS)
        pygame.draw.line(screen, (0, 0, 0), ((row + i) * cell_width, col * cell_width), ((row + i) * cell_width, col * cell_width + cell_width), SELECTED_CELL_THICKNESS)


def draw_board():
    """
    draw_board(): Draws the lines to make the board
    """
    # Known cells
    for i in range(9):
        for j in range(9):
            if test_display_grid[i][j] != 0:
                # Change color of known cells - OPTIONAL
                pygame.draw.rect(screen, (173, 216, 230), (row * cell_width, j * cell_width, cell_width + 1, cell_width + 1))

                # Place value in cell
                cell_val = font1.render(str(test_display_grid[i][j]), 1, (216, 230, 173))
                screen.blit(cell_val, (i * cell_width + VALUE_PADDING, j * cell_width + VALUE_PADDING))

    # Draw lines for grid
    for i in range(10):
        if i % 3 == 0:
            thickness = BORDER_THICKNESS
        else:
            thickness = CELL_THICKNESS
        
        # Grid starts at 0, 0 - can change later
        pygame.draw.line(screen, (0, 0, 0), (0, i * cell_width), (SCREEN_WIDTH, i *cell_width), thickness)
        pygame.draw.line(screen, (0, 0, 0), (i * cell_width, 0), (i * cell_width, SCREEN_WIDTH), thickness)
        

# TODO: COMBINE DRAW_VALUE AND INCORRECT_GUESS

def draw_value(val):
    """
    draw_value(val): Draws the given value in the selected cell.
    Drawn values are drawn in black. Whereas initial values are drawn in green.
    """
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (row * cell_width + VALUE_PADDING, col * cell_width + VALUE_PADDING))


def incorrect_guess(val):
    """
    incorrect_guess(val): When an incorrect value is placed in a cell the color of the value will change.
    """
    text1 = font1.render(str(val), 1, (255, 0, 0))
    screen.blit(text1, (row * cell_width + VALUE_PADDING, col * cell_width + VALUE_PADDING))


# Consider keyboard options instead of menu for starting new game.
# If keyboard options are used then use the instruction function below:
def instruction():
    """
    instruction(): Provides instructions to the user.
    Shows which keys are used for different options.
    """
    # Uses font2 to show instructions in larger font.
    # TODO: Use mouse or arrow keys to navigate cells? Or both?
    # TODO: Add other instructions as needed
    inst1 = font2.render("New Game Options: E for easy game, H for hard game, X for exper game", 1, (0, 0, 0))
    inst2 = font2.render("Use number keys to enter values, use arrow keys to navigate cells, use escape to quit", 1, (0, 0, 0))
    inst3 = font2.render("Use shift to toggle between candidates and guess", 1, (0, 0, 0))

    # TODO: Change where instructions are located.
    screen.blit(inst1, (20, SCREEN_HEIGHT-80))
    screen.blit(inst2, (20, SCREEN_HEIGHT-60))
    screen.blit(inst3, (20, SCREEN_HEIGHT-40))

def end():
    """
    end(): Displays a message when game is correctly completed.
    """
    text1 = font1.render("Complete!", 1, (0, 0, 0))
    # TODO: Change end font location?
    screen.blit(text1, (20, SCREEN_HEIGHT-20))

# error = 0
# If we want to show the number of error we can implement another method for it.
# def draw_error_count():

running = True
flag_cell = 0
difficulty = ''

while running:
    # Make the background - currently white
    screen.fill((255, 255, 255))

    # Control game with events
    for event in pygame.event.get():
        # Quitting the game
        if event.type == pygame.QUIT:
            running = False
        
        # If we use mouse to navigate cells:
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag_cell = 1
            coords = pygame.mouse.get_pos()
            get_cell(coords)

        # Key press instructions
        if event.type == pygame.KEYDOWN:
            # Quit Game With Escape
            if event.key == pygame.K_ESCAPE:
                running = False

            # Navigating With Arrow Keys
            if event.key == pygame.K_UP:
                row -= 1
                flag_cell = 1
            if event.key == pygame.K_DOWN:
                row += 1
                flag_cell = 1
            if event.key == pygame.K_LEFT:
                col -= 1
                flag_cell = 1
            if event.key == pygame.K_RIGHT:
                col += 1
                flag_cell = 1

            # Number Keys To Enter Values
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            
            # TODO: Shift (or other) for candidate toggle

            # TODO: Keys for starting new game w/ difficulties
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_h:
                pass
            if event.key == pygame.K_x:
                pass
    
    if val != 0:
        draw_value(val)

        # TODO: Check if valid here?

        val = 0
    
    draw_board()
    if flag_cell == 1:
        draw_cell()
    instruction()

    pygame.display.update()

pygame.quit()