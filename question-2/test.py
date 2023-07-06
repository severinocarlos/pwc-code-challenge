import unittest
from question import solve

class TestSuite(unittest.TestCase):
    def test_case_one(self):
        _input = 'Hello, World!'
        expected_output = 'Helo, Wrd!'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)
    
    def test_case_two(self):
        _input = 'PWC | Code Challenger'
        expected_output = 'PWC |odehalngr'

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)

    
if __name__ == '__main__':
    unittest.main()