import unittest
from question import solve

class TestSuite(unittest.TestCase):
    def test_one_case(self):
        _input = 'babad'
        expected_output = 'bab'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)
    
    def test_two_case(self):
        _input = 'abacabababad'
        expected_output = 'abacaba'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()