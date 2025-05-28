# def equlibrium(arr): #Time - O(n^2)
#     for i in range(len(arr)):#O(n)
#         left_sum = sum(arr[:i])
#         right_sum = sum(arr[i+1:])
#         print(left_sum, right_sum)

#         if left_sum == right_sum: #O(n)
#             return i

#     return -1

# arr = [-7, 1, 5, 2, -4, 3, 0]
# print(equlibrium(arr))

# optmial
def equlibrium(arr):
    left_sum = 0
    total_sum = sum(arr)
    for i, val in enumerate(arr):
        if left_sum == total_sum - left_sum - val:
            return i

        left_sum += val

    return -1


arr = [-7, 1, 5, 2, -4, 3, 0]
print(equlibrium(arr))

