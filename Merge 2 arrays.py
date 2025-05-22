def merge_sorted_arrays_brute_force(arr1, arr2):     #O((m + n) log(m + n)), space = O(m + n)
    merged = arr1 + arr2
    merged.sort()
    return merged

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
print(merge_sorted_arrays_brute_force(arr1, arr2))


def merge_arrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1

        else:

            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7, 8, 9, 10]
print(merge_arrays(arr1, arr2))

