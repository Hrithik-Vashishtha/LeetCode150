def isIsomorphi(s, t):
    dic_s = {}
    dic_t = {}
    for c1, c2 in zip(s, t):
        if (c1 in dic_s and dic_s[c1] != c2) or (c2 in dic_t and dic_t[c2] != c1):
            return False
        dic_s[c1] = c2
        dic_t[c2] = c1
    return True

s = "egg"
t = "add"
print(isIsomorphi(s, t))