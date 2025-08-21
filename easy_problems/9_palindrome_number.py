def is_palindrome(x: int) -> bool:
    left = 0
    right = -1
    if x >= 0:
        x_str = str(x)
        for i in range(len(x_str) // 2):
            print(x_str[left], x_str[right])
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1
        return True
    return False


print(is_palindrome(0))


# TODO БЫСТРОЕ РЕШЕНИЕ

# def isPalindrome(self, x: int) -> bool:
#     if x < 0 or (x % 10 == 0 and x != 0):
#         return False
#
#     reversed_half = 0
#     orginal_x = x
#
#     while x > reversed_half:
#         reversed_half = reversed_half * 10 + x % 10
#         x = x // 10
#
#     return x == reversed_half or x == reversed_half // 10
