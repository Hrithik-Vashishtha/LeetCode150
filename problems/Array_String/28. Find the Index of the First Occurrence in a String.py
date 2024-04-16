def strStr(haystack, needle):
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:
            temp = i
            j = 1
            i += 1
            while j < len(needle) and i < len(haystack):
                if haystack[i] != needle[j]:
                    i = temp + 1  # Reset i back to temp + 1
                    j = 1        # Reset j to 1 instead of 0
                    break
                i += 1
                j += 1
            if j == len(needle):
                return temp
        else:
            i += 1
    return -1

haystack = "mississippi"
needle = "issip"
print(strStr(haystack, needle))
