def search_insert(nums: list[int], target: int) -> int:
    if target <= nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)

    left = 0
    right = len(nums)

    while True:
        current = (left + right) // 2
        print(current)
        if nums[current - 1] < target <= nums[current]:
            return current
        if nums[current] < target:
            left = current + 1
        else:
            right = current - 1


print(search_insert(nums=[1, 4, 6, 7, 8, 9], target=6))
