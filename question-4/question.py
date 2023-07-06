def next_char(string: str, index: int) -> str:
    string_size = len(string) - 1

    return string[index+1] if index <= string_size else string[index]

def is_final_sentence(char: str) -> bool:
    return True if char == '.' or char == '?' or char == '!' else False

def get_capitalize_char(old_char: str) -> str:
    code = ord(old_char)
    new_char = chr(code - 32)

    return new_char

def capitalize_string(string: str) -> str:
    answer = ''
    string_size = len(string)
    next_sentence = False

    for index, char in enumerate(string):
        if index == 0:
            new_char = get_capitalize_char(char)
            answer += new_char
            continue
        
        if is_final_sentence(char):
            answer += char
            next_sentence = True
        elif next_sentence and char != ' ':
            next_sentence = False

            new_char = get_capitalize_char(char)
            answer += new_char
        else:
            answer += char
            
    return answer


print(capitalize_string("hello. how are you? i'm fine, thank you"))