def isPalindrome(s):
    new_s = ''.join(char for char in s if char.isalnum()).lower()
    i, j = 0, len(new_s) - 1
    while i < j:
        if new_s[i] != new_s[j]:
            return False
        i += 1
        j -= 1
    return True

print(isPalindrome(s))