def one(nums):
    if nums > 9:
       return nums + 1

    else:
        first = nums[0]
        li = [0] * nums
        print("0000", li)
        li[0] = first + 1
        return nums

print(one(199))