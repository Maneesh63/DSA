def move_zeros(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1
    for k in range(i, len(arr)):
        arr[k] = 0
    return arr


print(move_zeros([0, 0, 1, 2, 3, 4]))
