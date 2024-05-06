def minWindow(s, t):
    if t == "": return ""
    countT, window = {}, {}
    length_ = len(s) + 1
    res, l = [-1,-1], 0

    for c in t:
        countT[c] = countT.get(c, 0) + 1
    have, need = 0, len(countT)
    for r in range(len(s)):
        char = s[r]
        window[char] = window.get(char, 0) + 1
        if char in countT and countT[char] >= window[char]:
            have += 1
        while have == need:
            if r - l + 1 < length_:
                length_ = r - l + 1
                res = [l, r]
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r + 1] if length_ != float('inf') else ""
s = "adobecodebanc"
t = "abc"
print(minWindow(s, t))