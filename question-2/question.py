def isRepeted(frequencyMap: map, char: str) -> bool:
    return True if frequencyMap[char] > 1 else False

def remove_duplicate_char(string: str) -> str:
    frequencyMap = {}
    ans = ''
    
    for index, char in enumerate(string):
        if (char == ''):
            ans += char
            continue

        if char in frequencyMap.keys():
            frequencyMap[char] += 1
        else:
            frequencyMap[char] = 1

        if not isRepeted(frequencyMap, char):
            ans += char
    
    return ans