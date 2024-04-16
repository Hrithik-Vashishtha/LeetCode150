def removeDuplicates(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            nums.remove(nums[j])
        else:
            i += 1
            j += 1
    return len(nums)
nums = [1,1,2]
print(removeDuplicates(nums))