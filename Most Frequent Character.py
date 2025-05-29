
#optimal Time = O(n), space = O(k)
def most_frequent_char(chars):
    hash_map = {}  #O(1)
    for char in chars: #O(n)
        hash_map[char] = hash_map.get(char, 0) + 1

    return max(hash_map, key=hash_map.get) #O(k)

chars = "banana"
print(most_frequent_char(chars))


#brute force
# def most_frequent_char(chars):
#     max_count = 0
#     fin_char = 0
#     for i in chars:
#         count = 0
#         for j in chars:
#             if i == j:
#                 count += 1
#         if count > max_count:
#             max_count = count
#             fin_char = i
#
#     return fin_char

