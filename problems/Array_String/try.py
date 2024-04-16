def strStr(haystac, needle):
    i = 0
    res = -1
    while i < len(haystack):
        if haystack[i] == needle[0]:
            temp = i
            i += 1
            j = 1
            while j < len(needle) and i < len(haystack):
                if haystack[i] != needle[j]:
                    break
                i += 1
                j += 1
            if j == len(needle):
                return temp
            else:
                i = temp + 1
        else:
            i += 1
    return -1

haystack = "mississippi"
needle = "pi"
print(strStr(haystack, needle))