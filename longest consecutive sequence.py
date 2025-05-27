def longest_consecutive_sequence(arr):
    count = 1
    max_count = 0
    for i in range(len(arr)):
        if arr[i]+1 not in arr:
            break
        else:
            count += 1
            max_count = max(max_count, count)


    return max_count

arr = [1,2,3,4,8,9,7]
print(longest_consecutive_sequence(arr))






