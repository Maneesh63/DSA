def prefix(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    return prefix_sum


def main_method(arr, l, r):
    prefix_sum = prefix(arr)
    print(prefix_sum)
    if l == 0:
        return prefix_sum[r]
    else:
        return prefix_sum[r] - prefix_sum[l - 1]

arr = [1, 2, 3, 4, 5, 6]
print(main_method(arr, 0, 3))