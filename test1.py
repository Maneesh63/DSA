def dont_care(arr, k):
    n = len(arr) % k
    right = len(arr)-1
    left = 0
    while left < right:
          arr[left], arr[right] = arr[right], arr[left]
          left += 1
          right -= 1

    return arr
dont_care()
arr = [1, 2, 3, 4, 5]
print(dont_care(arr, 3))
