#-------------------------------------------------------------------
# game_window.py - Launches a game_window with a board in it.
#                  This class also has GUI widgets 
#
# Authors: Shadrac Reyes, Kelton Palmer, Kory Adams, Corey De Vany
#-------------------------------------------------------------------
from board import *
import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500,480))
pygame.display.set_caption("Sudoku")

#draw the lines
def draw(): 
    # Draw the lines
    return 0

  

#main game loop
run = True
while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()