# Longest substring without repeating characters
#bruteforce with hashset
# def longest_substring(char):
#     max_length = 0
#     for i in range(len(char)):
#         seen = set()
#         for j in range(i, len(char)):
#             if char[j] in seen:
#                 break
#             seen.add(char[j])
#             max_length = max(max_length, j - i + 1)
#
#     return max_length
#
#
# print(longest_substring("abcabc"))


#optimal - sliding window with hashmap
def longest_substring(char):
    max_length = 0
    seen = set()
    start = 0

    for end in range(len(char)):
        while char[end] in seen:
            seen.remove(char[start])
            start += 1

        seen.add(char[end])
        max_length = max(max_length, end - start + 1)

    return max_length
print(longest_substring("abcabc"))
