import unittest

from DutchNationalFlagProblem import sort_012


class DutchNationalFlagProblemTest(unittest.TestCase):

    def test_should_sort_correctly(self):
        sorted_array = sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2], sorted_array)

    def test_edge_case_only_one_number_repeated(self):
        sorted_array = sort_012([1, 1, 1])

        self.assertEqual([1, 1, 1], sorted_array)

    def test_edge_case_empty_input(self):
        sorted_array = sort_012([])

        self.assertEqual([], sorted_array)
