def removeDuplicates(nums):
    if len(nums) < 3:
        return len(nums)

    j = 2  # Start from the 3rd element
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
    return j


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums))