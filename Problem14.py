
# # Euler project Problem 14
# def create_chain(n):
#     chain = []
#     if n % 2 == 0:
#         chain.append(n)
#         while n != 1:
#             if n % 2 == 0:
#                 n /= 2
#             else:
#                 n = 3 * n + 1
#             chain.append(n)
#     else:
#         chain.append(n)
#         while n != 1:
#             if n % 2 == 0:
#                 n /= 2
#             else:
#                 n = 3 * n + 1
#             chain.append(n)
#     return chain
#
#
# max_starter = 0
# number = 2
# max_size = 0
#
# while number < 1000000:
#     sequence = create_chain(number)
#     # print(sequence[0])
#     if len(sequence) > max_size:
#         max_size = len(sequence)
#         max_starter = sequence[0]
#     number += 1
# print("Maximum starter with longest chain is : ", max_starter)
# print("Longest chain is : ", sequence)
