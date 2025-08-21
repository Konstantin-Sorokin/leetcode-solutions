def remove_element(nums, val):
    j = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    print(j)


remove_element([2, 3, 3, 2, 3], 3)
