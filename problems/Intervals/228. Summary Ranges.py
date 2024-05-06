def summaryRanges(nums):
    if len(nums) == 0:
        return []
    ranges = []
    start = nums[0]
    end = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(end))

            start = nums[i]
            end = nums[i]

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(str(start) + "->" + str(end))

    return ranges

nums = [0,1,2,4,5,7]
print(summaryRanges(nums))


