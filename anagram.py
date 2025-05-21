def anagram(str1, str2):
    s_str1 = sorted(str1)  # O(n log n)
    s_str2 = sorted(str2)  # O(m log n)
    if s_str1 == s_str2:  # O(k log n)
        return True
    else:
        return False


print(anagram("Maneesh", "hseenaM"))

# hence Time = O(k log k)     #space = 0(k)