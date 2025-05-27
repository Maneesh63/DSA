def subarray_equals_k(arr, k):
    count = 0
    h_map = {}
    prefix_sum = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            count += 1

        if prefix_sum - k in h_map:
            count += h_map[prefix_sum - k]
        h_map[prefix_sum] = h_map.get(prefix_sum, 0) + 1

    return count


arr = [1, 2, 3, 4, 5, 6]
k = 5
print(subarray_equals_k(arr, k))
