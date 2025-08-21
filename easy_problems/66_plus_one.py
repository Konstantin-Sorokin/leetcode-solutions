# def plus_one(digits: list[int]) -> list[int]:
#     new_num = 1
#     degree = 0
#
#     for i in range(len(digits) - 1, -1, -1):
#         new_num += digits[i] * 10**degree
#         degree += 1
#
#     return [int(digit) for digit in str(new_num)]


def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:

            digits[i] = digits[i] + 1
            return digits

    return [1] + digits


print(plus_one([8, 9, 9, 9, 3]))
