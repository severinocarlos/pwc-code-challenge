def isPalindrome(string: str) -> str:
    reversed_string = string[::-1]
    return True if string == reversed_string else False

def get_longest_palindromic_substring(string: str) -> str:
    substringsList = []
    string_size = len(string)
    answer = ''
    size_answer = 0
    
    # Caso o tamanho string for == 1, retorna a mesma string
    # Complexidade: O(n^2)
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
