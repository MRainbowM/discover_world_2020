import math
n = int(input())

f = math.factorial(n)
# while n > 1:
#     f *= n
#     n -= 1
d = 10 ** 6 + 3

x = (f % d + d) % d
print(x)