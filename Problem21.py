
# # Euler project Problem 21
# def sum_divisors(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return sum
#
#
# def amicable(a, b):
#     if sum_divisors(b) == a:
#         return True
#     else:
#         return False
#
#
# # def findSum(arr, n):
# #     # sort all elements of array
# #     arr.sort()
# #
# #     summ = arr[0]
# #     for i in range(0, n - 1):
# #         if (arr[i] != arr[i + 1]):
# #             summ = summ + arr[i + 1]
# #
# #     return summ
#
#
# result = 0
# n = 1
# list_of_amicables = []
# while n < 10000:
#     a = n
#     b = sum_divisors(a)
#     if amicable(a, b) and a != b:
#         list_of_amicables.append(a)
#         list_of_amicables.append(b)
#         result = result + a + b
#     n += 1
# print(result // 2)
# # size=len(list_of_amicables)
# # print(findSum(list_of_amicables,size))
