def remove_duplicates(nums: list[int | str]) -> int:
    idx = 0
    counter = len(nums) - 1
    while counter:
        if nums[idx] == nums[idx + 1]:
            del nums[idx + 1]
            nums.append("_")
        else:
            idx += 1
        counter -= 1
    return idx + 1


list_1 = [0, 1, 1, 2, 2, 2, 3, 4, 5, 5]

print(remove_duplicates(list_1))
