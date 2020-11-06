#-------------------------------------------------------------------
# board.py - Contains a 2-d array of cells for the gameboard, and various methods to modify it.
#
# Authors: Shadrac Reyes, Kelton Palmer, Kory Adams, Corey De Vany
#-------------------------------------------------------------------e
import array
import cell
from random import randrange
import numpy


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

    # Overload
    def __init__(self, file_name, difficulty):
        self.map = []
        for i in range(10):
            map.append([Cell()] * 9)
        self.map = Board()
        value_lists = read_from_file(file_name, difficulty)
        for line in value_lists:
            for value in line:
                

        

    #Puts value in cell
    def place_value(self, x_coord, y_coord, value):
        self.map[y_coord][x_coord].set_value(value)

    # Gets value in cell
    def get_value(self, x_coord, y_coord):
        return self.map[y_coord][x_coord].get_value()

    # Reads a game file into a 2-D int array
    def read_from_file(self, file_name, difficulty):
        # Sanitize input to lowercase
        difficulty = difficulty.lower()

        # Open a random game file
        directory = "game/" + difficulty + "/"
        game_number = randrange(3)+1
        game_file = directory + file_name + game_number
        file = open(game_file, "r")
        
        # Get lines from file
        lines = file.readlines()

        file_array = []

        # For each line in the line array, get an array of 
        # values, if the value is not zero, set the value
        # in that position.
        for line in lines:
            int_value_array = line.split()
            int_value_array = numpy.array(int_value_array).astype('int').tolist()
            file_array.append(int_value_array)

        file.close()

        return file_array
            

    #solves the sudoku puzzle
#    def solve(self):
#
    # def __is_for_row(self, row, value):

    # def __is_valid_for_col(self, col, value):

    # def __is_valid_for_box(self, row, col, value):

    # def __is_valid_for_position(self, row, col, value):

    # def __verify(self):

    # def __repr__(self):
        