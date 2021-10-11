import unittest
from MinMax import get_min_max


class MinMaxTest(unittest.TestCase):

    def test_find_min_max(self):
        minimum, maximum = get_min_max([4, 5, 3, 2, 9, 6, 7, 1, 8, 0])

        self.assertEqual(0, minimum)
        self.assertEqual(9, maximum)

    def test_should_raise_value_error_if_array_is_empty(self):
        self.assertRaises(ValueError, get_min_max, [])

    def test_should_return_same_number_if_array_length_is_one(self):
        minimum, maximum = get_min_max([9])

        self.assertEqual(9, minimum)
        self.assertEqual(9, maximum)
