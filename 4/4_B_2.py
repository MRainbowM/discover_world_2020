def f(a, b):
    if(a - b >= 0):
        return True
    else:
        return False

c = list(map(int, input().split(' ')))



X = (c[0] - c[2]) * (c[5] - c[3]) - (c[1] - c[3]) * (c[4] - c[2])

if (X == 0 and (f(c[0], c[2]) and f(c[0], c[4]) and f(c[2], c[0]) and f(c[4], c[0]))):
    print('YES')
else:
    print('NO')
# 	if((c[1] >= c[3] and c[1] <= c[5]) or (c[1] <= c[3] and c[1] >= c[5])):
# 		print('YES')
# 	else:
# 		print('NO')
# else:
# 	print('NO')

