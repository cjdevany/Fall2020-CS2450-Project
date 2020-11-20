import unittest
from src.cell import *

class Cell_Test(unittest.TestCase):

    def no_arg_const_test(self):
        expected = 'Value: 0 Key: 0 Candidates: [False, False, False, False, False, False, False, False, False, False]'
        self.assertEqual(Cell(), expected)

    def value_const_test(self):
        expected = 'Value: 1 Key: 1 Candidates: None'
        self.assertEqual(Cell(1), expected)

    def get_value_test(self):
        test_cell = Cell(1)
        self.assertEqual(1, test_cell.get_value())

    def set_value_test(self):
        test_cell = Cell()
        test_cell.set_value(1)
        cell_value = test_cell.get_value()
        self.assertEqual(1, cell_value)
    
    def get_key_test(self):
        test_cell = Cell(1)
        self.assertEqual(1, test_cell.get_key())

    def set_key_test(self):
        test_cell = Cell()
        test_cell.set_key(1)
        cell_key = test_cell.get_key()
        self.assertEqual(1, cell_key)

    def is_correct_true_test(self):
        test_cell = Cell(1)
        self.assertTrue(test_cell.is_correct())

    def is_correct_false_test(self):
        test_cell = Cell()
        test_cell.set_key(1)
        test_cell.set_value(5)
        self.assertFalse(test_cell.is_correct())

    def set_candidates_test(self):
        test_cell = Cell()
        test_cell.set_candidate(1, True)
        expected = 'Value: 0 Key: 0 Candidates: [False, True, False, False, False, False, False, False, False, False]'
        self.assertEqual(test_cell, expected)

    def get_candidates_test(self):
        test_cell = Cell()
        test_cell.set_candidate(1, True)
        self.assertEqual(test_cell.get_candidates, [1])
    
    def get_candidates_none_test(self):
        test_cell = Cell(1)
        self.assertIsNone(test_cell.get_candidates())

if __name__ == "__main__":
    unittest.main()