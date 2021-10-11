import unittest
from RearrangeArrayElements import rearrange_digits


class RearrangeArrayElementsTest(unittest.TestCase):

    def test_rearrangement(self):
        rearranged_digits = rearrange_digits([1, 2, 3, 4, 5])

        self.assertEqual((531, 42), rearranged_digits)

    def test_edge_case_only_one_number(self):
        rearranged_digits = rearrange_digits([9])

        self.assertEqual((9, 0), rearranged_digits)

    def test_edge_case_no_number(self):
        rearranged_digits = rearrange_digits([])

        self.assertEqual((0, 0), rearranged_digits)
