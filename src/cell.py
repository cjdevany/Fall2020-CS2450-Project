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
    def __init__(self):
        """ Null Constructor sets value and key to 0. """
        self.key = 0
        self.value = 0
        self.candidates = [False]*10

    def __init__(self, value):
        """ 
        Takes a value and assigns it to key and value. 
        This constructor is only used when the right answer is known at construction time.
        """
        self.key = value
        self.value = value
        # we don't need candidates, as this one is constructed with the right answer.
        self.candidates = None
    
    def __repr__(self):
        toStr = 'Value: ' + self.value + 'Key: ' + self.key + 'Candidates: ' + self.candidates
        return toStr
        
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
    
    def get_candidates(self):
        """ Returns this cells candidates as a list of integers for display purposes. """
        true_candidates = []
        for index, current_candidate in enumerate(self.candidates):
            if index >= 10:
                break

            if current_candidate:
                true_candidates.append(index)

        return true_candidates

    def set_candidate(self, index, value):
        """ Marks a candidate within the candidate list with the boolean value passed to it. """
        if(index < 1 or index > 9):
            pass
        else:
            self.candidates[index] = (bool)(value)
