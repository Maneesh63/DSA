def rm_dup(arr):
    store = []
    for i in arr:
        if arr[i] not in store:
            store.append(i)

    return store

arr = [2, 2, 2, 3, 3]
print(rm_dup(arr))
