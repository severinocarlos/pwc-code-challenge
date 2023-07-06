import unittest
from question import solve

class TestSuit(unittest.TestCase):
    def test_one_case(self):
        _input = 'racecar'
        expected_output = 'racecar'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)

    def test_two_case(self):
        _input = 'aabcaab'
        expected_output = 'baacaab'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()