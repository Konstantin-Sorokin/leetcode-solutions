def my_sqrt(x: int) -> int:
    left = 0
    right = x

    if x < 2:
        return x

    while True:

        cur = (left + right) // 2
        print(cur)
        if cur**2 > x:
            right = cur - 1
        elif cur**2 < x >= (cur + 1) ** 2:
            left = cur + 1
        elif cur**2 <= x < (cur + 1) ** 2:
            return cur // 1


print(my_sqrt(9))



# TODO другое решение
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         l, r = 1, x
#         mid = -1
#         while l <= r:
#             mid = (l + r) // 2
#             temp = mid * mid
#             if temp == x:
#                 return mid
#
#             elif temp > x:
#                 r = mid - 1
#
#             else:
#                 l = mid + 1
#
#         return r
