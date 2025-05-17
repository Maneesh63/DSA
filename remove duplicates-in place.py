def partition_even_odd(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
print(partition_even_odd([1,2,3,4,5,6]))