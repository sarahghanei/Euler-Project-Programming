# # Euler project Problem 4
# def is_palindrome(num):
#     num = str(num)
#     if num != num[::-1]:
#         return False
#     else:
#         return True
#
#
# temp = 0
# max_palindrome = 0
# for m in range(100, 1000):
#     for n in range(100, 1000):
#         temp = m * n
#         if is_palindrome(temp):
#             if temp > max_palindrome:
#                 max_palindrome = temp
# print(max_palindrome)
