values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

universal_val = "IXC"


def roman_to_int(s: str) -> int:
    number = 0

    for i, value in enumerate(s):
        current = values[value]
        if value in universal_val and i + 1 != len(s) and values[s[i + 1]] > current:
            number -= current
        else:
            number += current

    return number


print(roman_to_int("III"))
