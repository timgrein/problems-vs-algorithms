import unittest

from RotatedSortedArraySearch import rotated_array_search


class RotatedSortedArraySearchTest(unittest.TestCase):

    def setUp(self):
        self.array = [6, 7, 8, 9, 10, 1, 2, 3, 4]

    def test_should_return_negative_one_if_number_is_not_in_array(self):
        index = rotated_array_search(self.array, 5)

        self.assertEqual(-1, index)

    def test_should_return_five_as_index(self):
        index = rotated_array_search(self.array, 1)

        self.assertEqual(5, index)

    def test_should_return_negative_one_if_array_is_empty(self):
        index = rotated_array_search([], 1)

        self.assertEqual(-1, index)