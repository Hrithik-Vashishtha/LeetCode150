def maxArea(height):
    i, j = 0, len(height) - 1
    count = 0
    while i < j:
        min_height = min(height[i], height[j])
        length = j - i
        count = max(count, min_height * length)
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return count

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))