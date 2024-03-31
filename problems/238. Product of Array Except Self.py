def productExceptSelf(nums):
    prefix = [1] * len(nums)
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        prefix[i] = prefix[i] * postfix
        postfix = nums[i] * postfix
    return prefix
nums = [1,2,3,4]
print(productExceptSelf(nums))