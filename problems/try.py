def longestConsecutive(nums):
    num_index = {}
    for num in nums:
        num_index[num] = num_index.get(num, 0) + 1
    min_ = min(nums)
    max_ = max(nums)
    count = 0
    new_count = 0
    for i in range(min_, max_ + 1):
        if i not in num_index:
            count = max(new_count, count)
            new_count = 0
        else:
            new_count += 1
    return max(new_count, count)

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums))