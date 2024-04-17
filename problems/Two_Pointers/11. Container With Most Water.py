def maxArea(height):
    i, j = 0, len(height) - 1
    max_area = 0
    while i < j:
        length = j - i
        temp_height = min(height[i], height[j])
        new_area = length * temp_height
        max_area = max(max_area, new_area)
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))