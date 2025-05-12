import unittest
from function import (
    calculate_sum
)

class TestMathOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calculate_sum([1, 2, 3]), 6)
        self.assertEqual(calculate_sum([]), 0)
        self.assertEqual(calculate_sum([-1, 1]), 0)

if __name__ == '__main__':
    unittest.main()