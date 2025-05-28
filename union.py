# def union(arr1, arr2):
#     # brute force
#     result = []
#     for i in arr1:
#         if i not in result:
#             result.append(i)
#
#     for j in arr2:
#         if j not in result:
#             result.append(j)
#
#     return result
#
#
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [3, 4, 5, 6, 7, 8, 9, 10]
# print(union(arr1, arr2))
#

def union_with_set(arr1, arr2):
    result = set()
    for i in arr1:
        result.add(i)
    for j in arr2:
        result.add(j)
    return list(result)


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7, 8, 9, 10]
print(union_with_set(arr1, arr2))

#
# def union(arr1, arr2):
#     return list(set(arr1 + arr2))
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [3, 4, 5, 6, 7, 8, 9, 10]
# print(union(arr1, arr2))