import unittest
import numpy as np
from day5 import divide, which_seat

class TestDay5(unittest.TestCase):
    def test_divide_should_return_upper_half_values_if_value_is_F(self):
        # Given
        divide_val = 'F'
        possible_values = np.arange(128)
        expected = np.arange(64)

        # When
        remaining_vals = divide(possible_values, divide_val)

        # Then
        np.testing.assert_array_equal(remaining_vals, expected)

    def test_divide_should_return_upper_half_values_if_value_is_B(self):
        # Given
        divide_val = 'B'
        possible_values = np.arange(64)
        expected = np.arange(32, 64)

        # When
        remaining_vals = divide(possible_values, divide_val)

        # Then
        np.testing.assert_array_equal(remaining_vals, expected)

    def test_divide_should_return_upper_half_values_if_value_is_R(self):
        # Given
        divide_val = 'R'
        possible_values = np.arange(8)
        expected = np.arange(4, 8)

        # When
        remaining_vals = divide(possible_values, divide_val)

        # Then
        np.testing.assert_array_equal(remaining_vals, expected)

    def test_which_seat_should_return_correct_seat(self):
        # Given
        vals = "FBFBBFF"

        # When
        seat = which_seat(vals)

        # Then
        self.assertEqual(seat, 44)
