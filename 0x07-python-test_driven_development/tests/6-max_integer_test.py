#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integers(self):
        """A unittest cases for the function veracity"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -10]), -1)
        self.assertEqual(max_integer([-1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([11, 3, 24, 12]), 24)
        self.assertEqual(max_integer([189, 3, 4, 2]), 189)
        self.assertEqual(max_integer([6]), 6)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
