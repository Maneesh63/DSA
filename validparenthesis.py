def valid_parenthesis(s):

    hash_map = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    store = []
    for char in s:
        if char in hash_map.values():
            store.append(char)

        elif char in hash_map:
             if store[-1] != hash_map[char]:
                 return False

             store.pop()

    return len(store) == 0



print(valid_parenthesis("(){}[]"))
print(valid_parenthesis("({[]})"))



