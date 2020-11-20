import unittest
from board import *

class Board_Test(unittest.TestCase):

    def null_constructor_test(self):
        expected_output = []
        for i in range(10):
            expected_output.append([0]*9)
        self.assertEqual(Board(), expected_output)

    #def place_values_test(self):


if __name__ == "__main__":
    unittest.main()
    board = Board("easy\\easy1.txt")
    print(board)