def rotate_array_by_1_step(arr):
    if not arr:
        return arr
    last = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr

print(rotate_array_by_1_step([3, 5, 6, 1]))
