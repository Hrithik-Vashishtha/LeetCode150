def isSubsequence(s, t):
    j = 0
    for i in range(len(t)):
        if j < len(s) and t[i] == s[j]:
            j += 1
    return j == len(s)
s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))