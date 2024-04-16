def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

nums = [3,2,3]

print(majorityElement(nums))