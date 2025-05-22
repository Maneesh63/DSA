def missing(arr):
    for i in range(len(arr)-1):
        if arr[i+1] != arr[i] + 1:
            print(f"{arr[i]+1} is missing from an array")
            return False

    return True

arr = [1,2,3,4,6]
print(missing(arr))
