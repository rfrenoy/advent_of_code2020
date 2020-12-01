import unittest
from day1 import create_array, sums_to_value, find_values_adding_up_to_value

class TestDay1(unittest.TestCase):
    def test_create_array_should_create_array_from_buffer_entries(self):
        # Given
        buff = '1\n2\n3'
        expected = [1, 2, 3]

        # When
        arr = create_array(buff)

        # Then
        self.assertListEqual(arr, expected)

    def test_sums_to_value_return_true_if_args_sums_to_value_else_false(self):
        # Given
        inputs = [1, 2]
        val = 3
        false_val = 5

        # When
        t = sums_to_value(inputs, val)
        f = sums_to_value(inputs, false_val)

        # Then
        self.assertTrue(t)
        self.assertFalse(f)

    def test_find_values_adding_up_to_value_return_values_if_exists_or_none(self):
        # Given
        inputs = [1, 2, 3]
        nb_values = 2
        val = 4
        false_val = 7

        # When
        res = find_values_adding_up_to_value(inputs, nb_values, val)
        res2 = find_values_adding_up_to_value(inputs, nb_values, false_val)

        # Then
        self.assertListEqual(res, [1, 3])
        self.assertIsNone(res2)

