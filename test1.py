# def dont_care(arr, k):
#     n = len(arr) % k
#     right = len(arr)-1
#     left = 0
#     while left < right:
#           arr[left], arr[right] = arr[right], arr[left]
#           left += 1
#           right -= 1
#
#     return arr
# dont_care()
# arr = [1, 2, 3, 4, 5]
# print(dont_care(arr, 3))
#
# price = float(10000)
# print("Actual price:", price)
# discount_percentage = 10
#
# if not discount_percentage > 0 & discount_percentage <= 100:
#     print("Not a discount percentage")
#
#
# discount_amount = price/discount_percentage
# print(discount_amount)
# final_price = price - discount_amount
# print(final_price)