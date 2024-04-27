def containsNearbyDuplicate(nums, k):
    numDict = {}
    for num in nums:
        numDict[num] = numDict.get(num, 0) + 1
    for key, value in numDict.items():
        if value >= 2:
            i, j = 0, len(nums) - 1
            while i < j:
                if nums[i] == nums[j] and abs(j - i) <= k:
                    return True
                else:
                    j -= 1
    return False

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))