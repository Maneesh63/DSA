# def product_subarray(arr, k):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         current_product = 0
#         for j in range(i, n):
#             current_product *= arr[j]
#             if current_product <= k:
#                 count += 1
#     return count
#
# arr = [1,2,3,4]
# print(product_subarray(arr, 3))

#optmial
def product_subarray(arr, k):
    if k <= 1:
        return 0

    count = 0
    n = len(arr)
    left = 0
    current_product = 0
    for i in range(n):
        current_product *= arr[i]

        while current_product > k:
            current_product /= arr[i]
            left += 1

        count += i - left + 1
    return count

arr = [1,2,3,4]
print(product_subarray(arr, 3))


