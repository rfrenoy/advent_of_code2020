import unittest
import numpy as np
from day5 import which_seat

class TestDay5(unittest.TestCase):

    def test_which_seat_should_return_correct_seat(self):
        # Given
        vals = "FBFBBFF"

        # When
        seat = which_seat(vals)

        # Then
        self.assertEqual(seat, 44)
