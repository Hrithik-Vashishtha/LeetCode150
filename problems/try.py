# def wordPattern(pattern, s):
#     words = s.split()
#     if len(pattern) != len(words):
#         return False
#
#     char_to_word = {}
#     word_to_char = {}
#
#     for char, word in zip(pattern, words):
#         if char not in char_to_word:
#             if word in word_to_char:
#                 return False
#             char_to_word[char] = word
#             word_to_char[word] = char
#         else:
#             if char_to_word[char] != word:
#                 return False
#
#     return True
#
#
# # Example usage:
# pattern = "abba"
# s = "dog cat cat dog"
# print(wordPattern(pattern, s))  # Output: True















