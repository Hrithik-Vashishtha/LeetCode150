def isAnagram(s, t):
    s_dict = {}
    t_dict = {}
    for elem in s:
        s_dict[elem] = s_dict.get(elem, 0) + 1
    for elem in t:
        t_dict[elem] = t_dict.get(elem, 0) + 1

    if s_dict == t_dict:
        return True
    return False

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
