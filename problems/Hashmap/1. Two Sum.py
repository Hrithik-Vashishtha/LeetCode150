def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        num = target - nums[i]
        if num in dic:
            return ([i, dic[num]])
        dic[nums[i]] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
