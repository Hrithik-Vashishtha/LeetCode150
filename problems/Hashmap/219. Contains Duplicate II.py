def isAnagram(s, t):
    s_dic = {}
    t_dic = {}

    for i in s:
        s_dic[i] = s_dic.get(i, 0) + 1
    for i in t:
        t_dic[i] = t_dic.get(i, 0) + 1

    for i in s:
        if i in t_dic and s_dic[i] != t_dic[i]:
            return False
    return True

s = "rat"
t = "car"
print(isAnagram(s, t))