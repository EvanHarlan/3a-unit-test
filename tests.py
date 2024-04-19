# Import unit test
import unittest
from datetime import datetime
from user_input import UserInput
# Testing for user inputs
class userInputTest(unittest.TestCase):
    # Testing symbol from get_symbol funciton.
    def test_get_symbol_valid_input(self):
        user_input = UserInput()
        test_symbol = "GOOGL"
        actual_symbol = user_input.get_symbol()

        self.assertEqual(actual_symbol, test_symbol)

    # Test the is_Valid String method to make sure the string is invalid from get_symbvol
    def test_is_invalid_string(self):
        user_input = UserInput()
        invalid_string_input = ""
        
        self.assertFalse(user_input.isValidString(invalid_string_input))
    # Test the is_valid string method to make sure the string is valid
    def test_is_valid_string(self):
        user_input = UserInput()
        valid_string_input = "adsf"
        
        self.assertTrue(user_input.isValidString(valid_string_input))

    # Test to check valid date format
    def test_get_date_valid_format(self):
        user_input = UserInput()
        user_date = user_input.get_date('Start')

        self.assertIsInstance(user_date, datetime)


    # Testing for invalid date format
    def test_get_date_invalid_format(self):
        user_input = UserInput()
        
        with self.assertRaises(TypeError):
            user_input.get_date('Start', '2024-04-04')

    # Testing for invalid format
    # This raises an error becuase (04-04-2024) is an invalid format (Backwards from the original)
    def test_invalid_date_format(self):
        user_input = UserInput()

        with self.assertRaises(Exception):
            user_input.get_date('04-04-2024')

    # Testing date range function
    def test_get_valid_date_range(self):
        start_date = datetime(2024, 4, 10)
        end_date = datetime(2024, 4, 15)
        user_input = UserInput()

        self.assertTrue(user_input.valid_date_range(start_date, end_date))

    # Testing chart type function
    def test_get_valid_chart_type(self):
        user_input = UserInput()
        chart_type = user_input.get_time_series()

        self.assertTrue(user_input.isValidString(chart_type))

    # Testing the time series function
    def test_valid_time_series(self):
        user_input = UserInput()
        time_series = user_input.get_time_series()

        self.assertTrue(user_input.isValidString(time_series))


# Double underscore method / magic method
# Whenever executing a script, every script has a name. This will be called main becuase this is where the code execution originates.
if __name__ == '__main__':
    unittest.main()