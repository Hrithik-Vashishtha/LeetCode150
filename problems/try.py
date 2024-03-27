def canJump(nums):
    goal = len(nums) - 1
    i = len(nums) - 1
    while i >= 0:
        if nums[i] >= goal - i:
            goal = i
        elif goal <= 0:
            return True
        i -= 1
    if goal == 0:
        return True
    return False
nums = [2,3,1,1,4]
print(canJump(nums))