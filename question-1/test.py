import unittest
from question import reverse_string

class TestSuite(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(reverse_string('Hello, World! OpenAI is amazing.'), 'amazing. is OpenAI World! Hello,')

    def test_case_two(self):
        self.assertEqual(reverse_string('PWC | Code Challenge'), 'Challenge Code | PWC')
    
    def test_case_three(self):
        self.assertEqual(reverse_string('Code, Coffee and Algorithm!!'), 'Algorithm!! and Coffee Code,')

if __name__ == '__main__':
    unittest.main()