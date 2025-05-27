#optimal
def max_subarray_equals_k(arr, k):
    total_len = 0
    prefix_sum = 0
    sum_map = {}
    print("ARRAY ==>", arr)
    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            print("found target", prefix_sum)
            total_len = i + 1
            print("total len", total_len)

        if prefix_sum - k in sum_map:
            print("found target", prefix_sum - k)
            lenght = i - sum_map[prefix_sum - k]
            print("lenght", lenght)
            total_len = max(total_len, lenght)
            print("total len", total_len)

        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = i

    print("sum map", sum_map)
    print("final total len", total_len)
    return total_len
arr = [1, 2, 3, 1, 1, 1, 1]
print(max_subarray_equals_k(arr, 5))

#
# #bruteforce
# def max_subarray_equals_k(arr, k):
#     total_len = 0
#     for i in range(len(arr)):
#         current_sum = 0
#         for j in range(i , len(arr)):
#             current_sum += arr[j]
#             if current_sum == k:
#                 total_len = max(total_len, j-i+1)
#
#
#     return total_len
# arr = [1, 2, 3, 1, 1, 1, 1]
# print(max_subarray_equals_k(arr, 5))
#
# #Time = O(n^2)
# #space = O(1)
#
#
#
