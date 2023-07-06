import unittest
from question import solve

class TestSuite(unittest.TestCase):
  
    def test_one_case(self):
        _input = "hello. how are you? i'm fine, thank you."
        expected_output = "Hello. How are you? I'm fine, thank you."

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)

    def test_case_two(self):
        _input = "hello! my name is Severino. and you?"
        expected_output = "Hello! My name is Severino. And you?"

        output = solve(_input)
        print(f'Case:\nOutput: {output}    |   Expected Output: {expected_output}\n')
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()