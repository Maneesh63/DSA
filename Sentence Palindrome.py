#
# #time = O(n), space = O(n)
# def sentencePalindrome(sentence):
#
#     result = []
#     for char in sentence:
#         if char.isalpha():
#             result.append(char.lower())
#
#     new = "".join(result)
#     rev = new[::-1]
#
#     if new == rev:
#         return True
#
#     return False
# sentence = "Too hot to hoot."
# print(sentencePalindrome(sentence))


def sentencePalindrome2(sentence):
    left, right = 0, len(sentence)-1

    while left < right:
          if not sentence[left].isalpha():
              left += 1

          if not sentence[right].isalpha():
              right -= 1

          if sentence[left].lower() == sentence[right].lower():
              left += 1
              right -= 1

          else:
              return  False

    return True

sentence = "Too hot to hoot."
print(sentencePalindrome2(sentence))
