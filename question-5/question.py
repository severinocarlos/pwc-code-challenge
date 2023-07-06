def isPalindrome(string: str) -> str:
    reversed_string = string[::-1]
    return True if string == ''.join(reversed_string) else False

def swap(string, i, j):
    string[i], string[j] = string[j], string[i]

def anagrams_generator(string: list, curr_index=0) -> list:
    global answer
    string_size = len(string)

    if curr_index == string_size - 1:
        if isPalindrome(''.join(string)):
            answer = ''.join(string)
 
    for i in range(curr_index, string_size):
        swap(string, curr_index, i)
        anagrams_generator(string, curr_index + 1)
        swap(string, curr_index, i)

    return answer

def solve(string: str) -> str:
    charList = list(string)
    answer = anagrams_generator(charList)
    return answer