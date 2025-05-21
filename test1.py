def move(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    return arr

print(move([1,2,0,3,0,4,0,5]))