def smallest_subarray_with_sum(arr, target):
    left = 0
    current_sum = 0
    result = []

    for i in range(len(arr)):
        current_sum += arr[i]

        while current_sum > target:
              current_sum -= arr[left]
              left += 1

        if current_sum == target:
            result.append((left, i))

    return result

arr = [2, 3, 1, 2, 4, 3]
target = 7
print(smallest_subarray_with_sum(arr, target))
