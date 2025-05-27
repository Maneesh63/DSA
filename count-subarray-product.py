def product_subarray(arr, k):
    count = 0
    n = len(arr)
    for i in range(n):
        current_product = 0
        for j in range(i, n):
            current_product *= arr[j]
            if current_product <= k:
                count += 1
    return count

arr = [1,2,3,4]
print(product_subarray(arr, 3))
