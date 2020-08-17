# # Euler project Problem 10
# def is_prime(n):
#     res = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             res = False
#     return res
#
# n = 2
# sum_prime = 0
# while n < 2000000:
#     if is_prime(n):
#         sum_prime += n
#         print(sum_prime)
#     n += 1
# print(sum_prime)
