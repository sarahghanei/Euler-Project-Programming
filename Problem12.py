# Euler project Problem 12
# def is_prime(n):
#     res = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             res = False
#     return res
#
#
# def create_triangle(n):
#     res = 0
#     if n == 0:
#         res = 1
#     else:
#         while n != 0:
#             res += n
#             n -= 1
#     return res
#
#
# def divisors(num):
#     list_prime = []
#     for ii in range(2, int(num ** 0.5) + 1):
#         if num % ii == 0:
#             if is_prime(ii):
#                 list_prime.append(ii)
#     # print("list of prime divisors",list_prime)
#     list_power = []
#     for item in list_prime:
#         x = 0
#         while num % item == 0:
#             num = num / item
#             x+=1
#         list_power.append(x+1)
#     # print("list of powers",list_power)
#     div=1
#     for item in list_power:
#         div=div*item
#     return div
#
# newTerm = 0
# i = 0
# while True:
#     newTerm = create_triangle(i)
#     # print(newTerm)
#     # print(divisors(newTerm))
#     if divisors(newTerm) >= 500:
#         print(newTerm)
#         break
#     else:
#         i += 1
