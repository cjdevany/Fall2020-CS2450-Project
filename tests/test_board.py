import unittest
import board


class Board_Test(unittest.TestCase):

    def TEST_FILE_CONSTANT(self):
        return "/game/easy1.txt"

    def constructor_test(self):
        test_board = board(TEST_FILE_CONSTANT())
        expected_output =  [[0, 0, 2, 0, 0, 0, 5, 0, 0],
                            [0, 1, 0, 7, 0, 5, 0, 2, 0],
                            [4, 0, 0, 0, 9, 0, 0, 0, 7],
                            [0, 4, 9, 0, 0, 0, 7, 3, 0],
                            [8, 0, 1, 0, 3, 0, 4, 0, 9],
                            [0, 3, 6, 0, 0, 0, 2, 1, 0],
                            [2, 0, 0, 0, 8, 0, 0, 0, 4],
                            [0, 8, 0, 9, 0, 2, 0, 6, 0],
                            [0, 0, 7, 0, 0, 0, 8, 0, 0]]
        self.assertEqual(test_board, expected_output)

    def read_file_test(self):
        test_board = board()
        test_file_array =  [[0, 0, 2, 0, 0, 0, 5, 0, 0],
                            [0, 1, 0, 7, 0, 5, 0, 2, 0],
                            [4, 0, 0, 0, 9, 0, 0, 0, 7],
                            [0, 4, 9, 0, 0, 0, 7, 3, 0],
                            [8, 0, 1, 0, 3, 0, 4, 0, 9],
                            [0, 3, 6, 0, 0, 0, 2, 1, 0],
                            [2, 0, 0, 0, 8, 0, 0, 0, 4],
                            [0, 8, 0, 9, 0, 2, 0, 6, 0],
                            [0, 0, 7, 0, 0, 0, 8, 0, 0]]
        file_array = test_board.read_file(TEST_FILE_CONSTANT()) 
        self.assertEqual(test_file_array, file_array)
            

    def set_candidates_from_cell_test(self):
        test_board = board(TEST_FILE_CONSTANT())
        test_board.set_candidate(0, 0, 1, True)
        self.assertTrue(test_board.get_candidate(0, 0, 1))


    def get_candidates_from_cell_test(self):
        test_board = board()
        test_board.set_candidate(0, 0, 1, True)
        self.assertTrue(test_board.get_candidate(0, 0, 1))


    def set_value_in_cell_test(self):
        test_board = board(TEST_FILE_CONSTANT())
        test_board.set_value(0, 0, 1)
        cell_value = test_board.get_value(0, 0)
        self.assertEqual(1, cell_value)
            
    
    def get_value_from_cell_test(self):
        test_board = board(TEST_FILE_CONSTANT())
        cell_value = test_board.get_value(0, 0)
        self.assertEqual(0, cell_value)   
        
    
        
if __name__ == "__main__":
    unittest.main()
    board = Board("easy\\easy1.txt")
    print(board)