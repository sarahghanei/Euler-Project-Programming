
# # Euler project Problem 7
# def is_prime(n):
#     res = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             res = False
#     return res
#
#
# def nth_prime(n):
#     count = 0
#     ans = 0
#     number = 2
#     if n == 1:
#         return 2
#     else:
#         while count < n:
#             if is_prime(number):
#                 ans = number
#                 print(ans)
#                 count += 1
#             number += 1
#         return ans
#
#
# n = input("Enter your number, and i'll find the nth prime number")
# answer = nth_prime(int(n))
# # print(type(answer))
# print("the %ith prime number is :%i " % (int(n), answer))
