def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = "_"
        else:
            count += 1

    i = 0
    j = len(nums)-1
    while i<j:
        if nums[i] == "_":
            while nums[j] == "_" and i<j:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        i += 1
    return count

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))