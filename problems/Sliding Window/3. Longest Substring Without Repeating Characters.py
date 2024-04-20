def lengthOfLongestSubstring(s):
    char_index = {}
    max_length = 0
    l = 0
    for r in range(len(s)):
        if s[r] in char_index and char_index[s[r]] >= l:
            l = char_index[s[r]] + 1
        char_index[s[r]] = r
        max_length = max(max_length, r - l + 1)
    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))