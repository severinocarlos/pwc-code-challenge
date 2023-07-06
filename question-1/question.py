def reverse_string(string: str) -> str:
    words: list = string.split()

    reservedList = reversed(words)
    reverse_string = " ".join(reservedList)

    return reverse_string
