arr = input().split(" ")
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
d = int(arr[3])

n = a * d + b * c
n = n / (b * d)
m = 10 ** 9 + 7

x = (n % m + m) % m

print(x)