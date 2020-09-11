n = int(input())
list_x = [1]

while n != 1:
    list_x.append(int(n))
    if n % 3 == 0:
        n = n / 3
    elif n % 2 == 0:
        n = n / 2
    else:
        n = n - 1

list_x.sort()

answ = ""
answ = answ + str(len(list_x) - 1)
answ = answ + '\n'
for k in list_x:
    answ = answ + str(k) + ' '

print(answ)

