def smallest_subarray_with_sum(arr, target):
    start = 0
    curr_sum = 0
    min_len = float('inf')

    for end in range(len(arr)):
        curr_sum += arr[end]

        while curr_sum >= target:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return min_len if min_len != float('inf') else 0


arr = [2, 3, 1, 2, 4, 3]
target = 7
print(smallest_subarray_with_sum(arr, target))  # Output: 2 ([4,3])


#
# def smallest_subarray_with_sum_bruteforce(arr, target):
#     min_len = float('inf')
#     n = len(arr)
#
#     for start in range(n):
#         curr_sum = 0
#         for end in range(start, n):
#             curr_sum += arr[end]
#             if curr_sum >= target:
#                 min_len = min(min_len, end - start + 1)
#                 break
#
#     return min_len if min_len != float('inf') else 0
#
# arr = [2, 3, 1, 2, 4, 3]
# target = 7
# print(smallest_subarray_with_sum_bruteforce(arr, target))
