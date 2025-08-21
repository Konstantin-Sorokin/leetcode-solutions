def two_sum(nums: list[int], target: int):
    all_num = dict()
    for i, num in enumerate(nums):
        if target - num in all_num:
            return [all_num[target - num], i]
        all_num[num] = i

    return None


t_s = two_sum(nums=[2, 7, 11, 15], target=9)
print(t_s)
