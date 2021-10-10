import unittest

from SquareRoot import sqrt


class SquareRootTest(unittest.TestCase):

    def test_calculate_square_root_correctly(self):
        square_root = sqrt(16)

        self.assertEqual(4, square_root)

    def test_calculate_square_root_correctly_floored(self):
        square_root = sqrt(27)

        self.assertEqual(5, square_root)

    def test_calculate_square_root_correctly_for_zero(self):
        square_root = sqrt(0)

        self.assertEqual(0, square_root)

    def test_raise_value_error_if_number_is_negative(self):
        self.assertRaises(ValueError, sqrt, -10)

    def test_raise_value_error_if_None_number_is_provided(self):
        self.assertRaises(ValueError, sqrt, None)
