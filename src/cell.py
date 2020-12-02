#-------------------------------------------------------------------
# cell.py - Contains the methods for the cell object.
#
# Authors: Shadrac Reyes, Kelton Palmer, Kory Adams, Corey De Vany
#-------------------------------------------------------------------

"""
A Cell has a key, a value, and a bool array for current candidates.
Key represents the correct answer for that cell
Value is the current cell's value
The bool array's indices represent if an integer is within the candidates list or not.
"""

class Cell:
    def __init__(self, value=0):
        """ 
        Takes a value and assigns it to key and value. 
        """
        self.key = value
        self.value = value
        self.candidates = [False]*10
        self.index = -1
    
    def __repr__(self):
        return str(self.value)

    def get_value(self):
        """ Returns current cell value """
        return self.value
    
    def set_value(self, _value):
        """ Sets this cells current value """
        self.value = _value

    def get_key(self):
        """ Returns this cells key """
        return self.key

    def set_key(self, _key):
        """ Sets this cells key """
        self.key = _key
    
    def is_correct(self):
        """ Returns true if a key is not null, and key == value. """
        if(self.key != None):
            return (self.key == self.value)
        else:
            return False
    
    def get_candidate(self, index):
        """ Returns True/False if a candidate is present within a cell. """
        return candidates[index]

    def set_candidate(self, index, value):
        """ Marks a candidate within the candidate list with the boolean value passed to it. """
        if(index < 1 or index > 9):
            pass
        else:
            self.candidates[index] = (bool)(value)
