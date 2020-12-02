#-------------------------------------------------------------------
# board.py - Contains a 2-d array of cells for the gameboard, and various methods to modify it.
#
# Authors: Shadrac Reyes, Kelton Palmer, Kory Adams, Corey De Vany
#-------------------------------------------------------------------e
import array
from cell import Cell
from random import randrange
import numpy


"""
The board has a map, and methods to interact with the map.
A map is a 9x9 2-d array of Cell objects.
"""

class Board:

    # Overload
    def __init__(self, file_name="easy1_sol.txt"):
        self.map = []
        self.values = self.read_file(file_name)
        for line in self.values:
            l = []
            for value in line:
                l.append(Cell(value))
            
            self.map.append(l)



    def __iter__(self):
        return (cell for cell in self.map)


    # Reads a game file into a 2-D int array
    def read_file(self, file_name):
        """
        Reads a board game info from a file and returns a 2d array of those values.

        Keyword arguments:
        file_name: the name of the file we are reading
        """
        file_array = []

        # Open the file
        game_file = "game/" + file_name
        file = open(game_file, "r")
        
        # Get lines from file
        lines = file.readlines()

        file.close()

        # Iterate over each line in the file
        for line in lines:
            # Remove the newline and spaces
            line = line.rstrip('\n')
            line = line.replace(" ", "")

            # Convert the string into a list of ints
            line = list(map(int, line))

            # Put the line into the file array.
            file_array.append(line)

        return file_array

    def __repr__(self):
        """ Returns a string representation of our map values. """
        rep = []

        for row in self.map:
            row_string = ''
            
            for col in row:
                row_string += str(self.map[row][col].get_value())
                row_string += ' '

            rep.append(row_string)
        return rep

    #Puts value in cell
    def set_value(self, x_coord, y_coord, value):
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

    # Returns the entire board
    def get_board(self):
        return self.map


    def set_candidate(self, x_coord, y_coord, candidate, value):
        """
        Given a (x, y) position in the 2d array representation of the game map
        marks a candidate within the candidate list with the boolean value passed to it.

        Keyword arguments:
        x_coord: The x-coordinate in the 2d array.
        y_coord: The y-coordinate in the 2d array.
        index: The index in the candidates array that will be set to value
        value: Boolean value an index within the candidates array will be set to
        """
        self.map[y_coord][x_coord].set_candidate(candidate-1, value)
    
    def get_candidate(self, x_coord, y_coord, candidate):
        """
        Given a (x, y) position of a cell in the 2d array representation of the game map
        gets the boolean value of a specific candidate within the cell.

        Keyword arguments:
        x_coord: The x-coordinate in the 2d array.
        y_coord: The y-coordinate in the 2d array.
        candidate: The candidate whose value is needed.
        """
        return self.map[y_coord][x_coord].get_candidate(candidate-1)
            
    #solves the sudoku puzzle
    # def solve(self):

    # def __is_valid_for_row(self, row, value):
        
        
    # def __is_valid_for_col(self, col, value):
        

    # def __is_valid_for_box(self, box_start_row, col_start_row, value):
        

    # def __is_valid_for_position(self, row, col, value):

    # def __verify(self):

    def print(self):
        for cell in self.map:
            print(cell)

if __name__ == "__main__":
    b = Board('easy1_sol.txt')
    b.print()