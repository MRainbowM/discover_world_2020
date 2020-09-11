import math
c = list(map(int, input().split(' ')))


X = (c[0] - c[2]) * (c[5] - c[3]) - (c[1] - c[3]) * (c[4] - c[2])
# x y x1 y1 x2 y2


# AB = c[4] - c[2]

# AB = c[2] * c[5] - c[4] * c[3]
# AX = c[2] * c[1] - c[0] * c[3]

# AX = c[0] * c[2] + c[1] * c[3]
# BX = c[0] * c[4] + c[1] * c[5]


AX = []
AX.append(c[0] - c[2])
AX.append(c[1] - c[3])
BX = []
BX.append(c[0] - c[4])
BX.append(c[1] - c[5])


# AX = math.sqrt((c[0] - c[2]) ** 2 + (c[1] - c[3]) ** 2)
# BX = math.sqrt((c[0] - c[4]) ** 2 + (c[1] - c[5]) ** 2)

# AXBX =

AXBX_1 = AX[0] * BX[0] + AX[1] * BX[1]
AXBX_2 = math.sqrt(AX[0]**2 + BX[0]**2) * math.sqrt(AX[1]**2 + BX[1]**2)
AXBX = AXBX_1 / AXBX_2
if(AXBX <= 0 and X ==0):
    print('YES')
else:
    print('NO')
    # if(X == 0 and AX <= 0 and BX <= 0):
    #     print('YES')
    # else:
    #     print('NO')
