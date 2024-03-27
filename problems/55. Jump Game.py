def canJump(nums):
    goal = len(nums) - 1
    i = len(nums) - 2
    while i >= 0:
        if nums[i] >= goal - i:
            goal = i
        i -= 1
    return True if goal == 0 else False