import unittest
from question import get_longest_palindromic_substring

class TestSuit(unittest.TestCase):
    def test_one_case(self):
        output = get_longest_palindromic_substring('babad')
        self.assertEqual(output, 'bab')
    
    def test_two_case(self):
        output = get_longest_palindromic_substring('abacabababad')
        self.assertEqual(output, 'abacaba')

if __name__ == '__main__':
    unittest.main()