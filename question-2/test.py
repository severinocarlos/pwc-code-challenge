import unittest
from question import remove_duplicate_char

class TestSuit(unittest.TestCase):
    def test_case_one(self):
        output = remove_duplicate_char('Hello, World!')
        self.assertEqual(output, 'Helo, Wrd!')

        print(f'OUTPUT 1: {output}')

if __name__ == '__main__':
    unittest.main()