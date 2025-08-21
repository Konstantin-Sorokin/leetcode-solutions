def add_binary(a: str, b: str) -> str:
    degree = 0
    number = 0

    for i in range(len(a) - 1, -1, -1):
        number += int(a[i]) * 2**degree
        degree += 1

    degree = 0

    for i in range(len(b) - 1, -1, -1):
        number += int(b[i]) * 2**degree
        degree += 1

    new_num = ""
    while number > 1:
        digit = number % 2
        number //= 2
        new_num = str(digit) + new_num

    return str(number) + new_num


print(add_binary("11", "1"))


# TODO лучшее решение
# def addBinary(self, a: str, b: str) -> str:
#     return bin(int(a, 2) + int(b, 2))[2:]

# print(int("11", 2))
# print(bin(4))
