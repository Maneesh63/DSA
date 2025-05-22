# def maximumCons(nums):
#     count = 0
#     for i in range(len(nums)):
#         current_count  = 0
#         for j in range(i, len(nums)):
#             if nums[j] == 1:
#                 current_count += 1
#                 count = max(count, current_count)
#             else:
#                 count = 0
#     return count
#
# arr = [1,1,1,3,4,1,1,2,6,1,1,1,1,1]
# print(maximumCons(arr))


def maximumCons(nums):
    left = 0
    count = 0
    for right in range(len(arr)):
        current_count = 0
        while right < len(arr):
               if nums[right] == 1:
                   current_count += 1
                   count = max(count, current_count)

               else:
                   count = 0

        left += 1

    return count



arr = [1,1,1,3,4,1,1,2,6,1,1,1,1,1]
print(maximumCons(arr))


