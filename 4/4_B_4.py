# while True:
c = list(map(int, input().split(' ')))
X = (c[0] - c[2]) * (c[5] - c[3]) - (c[1] - c[3]) * (c[4] - c[2])
AX = []
AX.append(c[0] - c[2])
AX.append(c[1] - c[3])
BX = []
BX.append(c[0] - c[4])
BX.append(c[1] - c[5])

AXBX = AX[0] * BX[0] + AX[1] * BX[1]

if(AXBX <= 0 and X ==0):
    print('YES')
else:
    print('NO')
