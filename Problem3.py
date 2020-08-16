# # Euler project Problem 3
# def is_prime(n):
#     res = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             res = False
#     return res
#
#
# def max_prime_factor(n):
#     max_prime = 0
#     while n % 2 == 0:
#         max_prime = 2
#         n /= 2
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         while n % i == 0:
#             max_prime = i
#             n = n / i
#             n = int(n)
#     return max_prime
#
#
# num = input("Enter your number : ")
# num = int(num)
# print("The maximum prime factor of %i is %i" % (num, max_prime_factor(num)))

