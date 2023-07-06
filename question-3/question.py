# Complexity: O(n^2)

def isPalindrome(string: str) -> str:
    reversed_string = string[::-1]
    return True if string == reversed_string else False

def solve(string: str) -> str:
    substringsList = []
    string_size = len(string)
    answer = ''
    size_answer = 0
    
    if string_size == 1:
        return string

    for index in range(string_size):
        substringsList.append(string[0: index+1])
        new_string = substringsList[index]

        if isPalindrome(new_string):
            new_string_size = len(new_string)
            if new_string_size > size_answer:
                answer, size_answer = new_string, new_string_size

    return answer
