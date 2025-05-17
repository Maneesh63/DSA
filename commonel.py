def common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print("Common elements:", common_elements(arr1, arr2))
