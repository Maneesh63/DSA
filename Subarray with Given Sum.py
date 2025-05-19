#brute force
def given_sum(arr, target):
    for i in range(len(arr)):
        current = 0
        for j in range(i, len(arr)):
            current +=arr[j]
            if current == target:
                return [i, j]


arr = [1, 2, 3, 4, 5]
print(given_sum(arr, 9))


#sliding window
def given_sum(arr, target):
    left = 0
    current = 0
    for right in range(len(arr)):
        current += arr[right]

        while current > target:
            current -= arr[left]
            left += 1

        if current == target:
            return [left, right]

    return -1


arr = [1, 2, 3, 4, 5]
print(given_sum(arr, 9))
