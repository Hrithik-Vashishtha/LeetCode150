def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in numSet:
            length = 1
            while n + length in numSet:
                length += 1
            longest = max(length, longest)
    return longest

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))