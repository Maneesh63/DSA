def non_repeat(char):
    seen = {}
    for i in char:  # O(n)
        if i not in seen:  # O(1)
            seen[i] = 1
        else:
            seen[i] += 1

    for dic in seen:
        if seen[dic] == 1:
            return i


print(non_repeat("mmaah"))