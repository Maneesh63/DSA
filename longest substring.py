# Longest substring without repeating characters
#bruteforce with hashset
def longest_substring(char):
    max_length = 0
    for i in range(len(char)):
        seen = set()
        for j in range(i, len(char)):
            if char[j] in seen:
                break
            seen.add(char[j])
            max_length = max(max_length, j - i + 1)

    return max_length


print(longest_substring("abcabc"))

#brutef