#brute force #time O(n^2)
def product_except_self(arr):
    result = []
    n =len(arr)
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= arr[j]
        result.append(product)

    return result

arr = [1, 2, 4, 5, 6, 7]
print(product_except_self(arr))
