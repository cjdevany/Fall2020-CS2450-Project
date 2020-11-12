#-------------------------------------------------------------------
# board.py - Contains a 2-d array of cells for the gameboard, and various methods to modify it.
#
# Authors: Shadrac Reyes, Kelton Palmer, Kory Adams, Corey De Vany
#-------------------------------------------------------------------e
from array import *
from .cell import Cell
from random import randrange

"""
The board has a map, and methods to interact with the map.
A map is a 9x9 2-d array of Cell objects.
"""

class Board:

    #constructs an empty map
    def __init__(self):
        self.map = []
        for i in range(10):
            map.append([Cell()] * 9)

    
    def __init__(self, file_name):
        

    #Puts value in cell
    def place_value(self, x_coord, y_coord):

    #Gets value in cell
    def get_value(self, x_coord, y_coord):

    #Reads file to a 2-D array
    def read_from_file(self, file_name, difficulty):
        lower_difficulty = difficulty.lower()
        directory = "game/" + lower_difficulty + "/"
        game_number = randrange(3)+1
        game_file = directory + file_name + game_number
        file = open(game_file, "r")
        
        if lower_difficulty == 'easy':
            
        if lower_difficulty == 'medium':

        if lower_difficulty == 'hard':
        
        file.close()

    #solves the sudoku puzzle
    def solve(self):