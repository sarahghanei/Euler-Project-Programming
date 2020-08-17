# Euler project Problem 9
def check_result(n1, n2, n3):
    res = False
    if n1 + n2 + n3 == 1000:
        res = True
    return res


for num1 in range(1, 1000):
    for num2 in range(num1, 1000 - num1):
        num3 = 1000 - num1 - num2
        if num1 ** 2 + num2 ** 2 == num3 ** 2:
            print("The product of Pythagorean triplet is : %i" % (num1 * num2 * num3))
