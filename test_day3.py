import unittest
from day3 import duplicate_input, elements

class TestDay3(unittest.TestCase):
    def test_duplicate_input_should_stack_horizontally_by_the_given_multiplicator(self):
        # Given
        arr = ['abcd', 'efgh']
        mul = 3
        expected = ['abcdabcdabcd', 'efghefghefgh']

        # When
        res = duplicate_input(arr, mul)

        #Then
        self.assertListEqual(res, expected)

    def test_elements_should_return_the_elements_down_the_given_slopes(self):
        # Given
        mat = ['abcdabcdabcd', 'efghefghefgh', 'ijklijklikjl']
        slope_down = 1
        slope_right = 3

        # When
        elts = elements(mat, slope_down, slope_right)

        # Then
        self.assertEqual(elts, 'hk')
