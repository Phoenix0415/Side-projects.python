import unittest
from unittest.mock import patch
from dice_roll_game import num_die

class TestDiceRollGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_num_die_single_die(self, mock_input):
        result = num_die()
        self.assertEqual(result, '1')

    @patch('builtins.input', side_effect=['2'])
    def test_num_die_double_die(self, mock_input):
        result = num_die()
        self.assertEqual(result, '2')

    @patch('builtins.input', side_effect=['three', '1'])  # first input is invalid, second is valid
    def test_num_die_invalid_input(self, mock_input):
        result = num_die()
        self.assertEqual(result, '1')

if __name__ == '__main__':
    unittest.main()
