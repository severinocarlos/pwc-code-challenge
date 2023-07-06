import unittest
from question import solve

class TestSuite(unittest.TestCase):

    def test_case_one(self):
        _input = 'Hello, World! OpenAI is amazing.'
        expected_output = 'amazing. is OpenAI World! Hello,'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)

    def test_case_two(self):
        _input = 'PWC | Code Challenge'
        expected_output = 'Challenge Code | PWC'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)
    
    def test_case_three(self):
        _input = 'Code, Coffee and Algorithm!!'
        expected_output = 'Algorithm!! and Coffee Code,'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()