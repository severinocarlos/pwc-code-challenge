import unittest
from exercise import solve

class TestSuit(unittest.TestCase):
    def test_one_case(self):
        _input = 'racecar'
        expected_output = 'racecar'
        self.assertEqual(solve(_input), expected_output)

    def test_two_case(self):
        _input = 'aabcaab'
        expected_output = 'baacaab'
        self.assertEqual(solve(_input), expected_output)

if __name__ == '__main__':
    unittest.main()