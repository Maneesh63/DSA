# # Python program to find the longest common prefix
# # using Sorting
#
# def longestCommonPrefix(arr):
#
#     # Sort the list of strings
#     arr.sort()
#
#     # Get the first and last strings after sorting
#     first = arr[0]
#     last = arr[-1]
#     minLength = min(len(first), len(last))
#     print("minLength", minLength)
#
#
#     i = 0
#     # Find the common prefix between the first
#     # and last strings
#     while i < minLength and first[i] == last[i]:
#         i += 1
#
#     # Return the common prefix
#     return first[:i]
#
# if __name__ == "__main__":
#     arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
#     print( longestCommonPrefix(arr))

def common_prefix(chars):
    result = ""
    for i in range(len(chars[0])):
        char = chars[0][i]

        for s in chars[1:]:
            if char != s[i]:
                return result

        result += chars[0][i]

    return result

chars = ["lowth", "lower", "lowest"]
print(common_prefix(chars))