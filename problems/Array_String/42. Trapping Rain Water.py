def trap(height):
    n = len(height)
    leftArray = [0 for i in range(n)]
    rightArray = [0 for i in range(n)]
    for i in range(1, n):
        leftArray[i] = max(height[i - 1], leftArray[i - 1])
    for i in range(n - 2, -1, -1):
        rightArray[i] = max(height[i + 1], rightArray[i + 1])
    count = 0

    for i in range(1, n - 1):
        if height[i] < leftArray[i] and height[i] < rightArray[i]:
            waterLevel = min(leftArray[i], rightArray[i])
            count += waterLevel - height[i]
    return count
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))