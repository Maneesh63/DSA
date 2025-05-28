#kadens algorithm
def maximum_subarray(arr):

    current_sum = 0
    total_sum = float('-inf')

    for num in arr:
        current_sum = max(current_sum, num + current_sum)  # 1, 1+0 -> 2, 2+1 = 3 -> 3, 3+3 = 6 -> 4, 4+6 = 10, -> 5, 5+10 = 15
        print("current sum on every itertaion", current_sum)
        total_sum = max(total_sum, current_sum)
        print("total sum on evry itertaion is:", total_sum)

    return total_sum

print(maximum_subarray([1, 2, 3, 4, 5]))


