string = input()
str_ar = string.split(' ')

n = int(str_ar[0])
m = int(str_ar[1])

n = n ** n
x = (n % m + m) % m
print(x)