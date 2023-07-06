# Complexity: O(n)

def isRepeted(frequencyMap: map, char: str) -> bool:
    return True if frequencyMap[char] > 1 else False

def solve(string: str) -> str:
    frequencyMap = {}
    answer = ''
    
    for index, char in enumerate(string):
        if (char == ''):
            answer += char
            continue

        if char in frequencyMap.keys():
            frequencyMap[char] += 1
        else:
            frequencyMap[char] = 1

        if not isRepeted(frequencyMap, char):
            answer += char
    
    return answer