# def maximum_subarray(arr, k):    #brute force approach
#     max_lenght = 0
#     for i in range(len(arr)):
#         current_sum = 0
#         for j in range(i, len(arr)):
#             current_sum += arr[j]
#             if current_sum <= k:
#                max_lenght = max(max_lenght, j-i+1)
#     return max_lenght
# print(maximum_subarray([1,2,3,4,5,6], 7))


def maximum_subarray(arr, k):
    left = 0
    current_sum = 0
    max_lenght = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        if current_sum > k:
              current_sum -= arr[left]
              left += 1

        max_lenght = max(max_lenght, right - left + 1)

    return max_lenght

print(maximum_subarray([1,2,3,4,5,6], 7))

