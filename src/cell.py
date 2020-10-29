#-------------------------------------------------------------------
# cell.py - Contains the methods for the cell object.
#
# Authors: Shadrac Reyes, Kelton Palmer, Kory Adams, Corey De Vany
#-------------------------------------------------------------------

"""
A Cell has a key, a value, and a bool array for current candidates.
Key represents the correct answer for that cell
Value is the current cell's value
The bool array's indeces represent if an integer is within the candidates list or not.
"""

class Cell:
    # null constructor - 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.candidates = [False]*10

    # value constructor
    def __init__(self, value):
        self.key = value
        self.value = value
        # we don't need candidates, as this one is constructed with the right answer.
        self.candidates = None
        
    # returns current value
    def get_value(self):
        return self.value
    
    # sets current value
    def set_value(self, _value):
        self.value = _value

    # returns the key of the cell
    def get_key(self):
        return self.key

    def set_key(self, _key):
        self.key = _key
    
    #returns true if key is not null and is equal to the correct value.
    def is_correct(self):
        if(self.key != None):
            return (self.key == self.value)
        else:
            return False
    
    # returns our current candidates as a list of integers
    def get_candidates(self):
        true_candidates = []
        for index, current_candidate in enumerate(self.candidates):
            if index >= 10:
                break

            if current_candidate:
                true_candidates.append(index)

        return true_candidates
