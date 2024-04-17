def isSubsequence(s, t):
    i = 0
    while i < len(t):
        if t[i] == s[0]:
            temp = i
            i += 1
            j = 1
            while i < len(t) and j < len(s):
                if t[i] != s[j]:
                    i = temp + 1
                    break
                i += 1
                j += 1
        else:
            i += 1
    return True if j == len(s) else False

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))