def solve(string: str) -> str:
    words: list = string.split()

    reversedList = reversed(words)
    reversed_string = " ".join(reversedList)

    return reversed_string
