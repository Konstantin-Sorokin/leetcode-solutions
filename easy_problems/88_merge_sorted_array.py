# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
#
#     res_len = m + n
#     nums1[:] = nums1[:m]
#     current_idx = 0
#     while len(nums1) < res_len and nums2:
#         number = nums2.pop(0)
#         print(current_idx, number)
#         while len(nums1) > current_idx and nums1[current_idx] < number:
#             current_idx += 1
#         nums1.insert(current_idx, number)
#
#     print(nums1)


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
    nums1[m:] = nums2
    nums1.sort()
    print(nums1)


n1 = [1, 2, 3, 0, 0, 0]
m = 3
n2 = [2, 5, 6]
n = 3


merge(n1, m, n2, n)
