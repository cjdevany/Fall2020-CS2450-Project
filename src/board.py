#-------------------------------------------------------------------
# board.py - Contains a 2-d array of cells for the gameboard, and various methods to modify it.
#
# Authors: Shadrac Reyes, Kelton Palmer, Kory Adams, Corey De Vany
#-------------------------------------------------------------------e
import array
from src.cell import *
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
    def __init__(self, file_name):
        self.map = []
        for i in range(10):
            map.append([Cell()] * 9)
        
        value_lists = self.read_file(file_name)
        for line, line_index in value_lists:
            for value, val_index in line:   
                if (value != 0):
                    map[line_index][val_index] = Cell(value)
                else:
                    map[line_index][val_index] = Cell()


    # Reads a game file into a 2-D int array
    def read_file(file_name="easy1.txt"):
        """
        Reads a board game info from a file and returns a 2d array of those values.

        Keyword arguments:
        file_name: the name of the file we are reading
        """

        # Open the file
        game_file = "..\\game\\" + file_name
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

    def __repr__(self):
        """ Returns a string representation of our map values. """
        rep = []

        for row in self.map:
            row_string = ''
            for col in row:
                row_string += str(self.map[row][col].get_value)
                row_string += ' '

            rep.append(row_string)
        return rep

    #Puts value in cell
    def place_value(self, x_coord, y_coord, value):
        """
        Places a given value at a given (x,y) position in the
        2d array representation of the game map.

        Keyword arguements:
        x_coord: The desired x-coordinate.
        y_coord: The desired y-coordinate.
        value: The value to be placed at this position.
        """
        self.map[y_coord][x_coord].set_value(value)

    # Gets value in cell
    def get_value(self, x_coord, y_coord):
        """
        Returns the value at the specified location.

        Keyword arguments:
        x_coord: The x-coordinate in the 2d array.
        y_coord: The y-coordinate in the 2d array.
        """
        return self.map[y_coord][x_coord].get_value()


            

    #solves the sudoku puzzle
#    def solve(self):

    # def __is_for_row(self, row, value):

    # def __is_valid_for_col(self, col, value):

    # def __is_valid_for_box(self, row, col, value):

    # def __is_valid_for_position(self, row, col, value):

    # def __verify(self):
