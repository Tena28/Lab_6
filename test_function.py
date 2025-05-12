import unittest
from function import (
    calculate_sum,
    calculate_difference
)

class TestMathOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calculate_sum([1, 2, 3]), 6)
        self.assertEqual(calculate_sum([]), 0)
        self.assertEqual(calculate_sum([-1, 1]), 0)

    def test_difference(self):
        self.assertEqual(calculate_difference(10, 5), 5)

if __name__ == '__main__':
    unittest.main()