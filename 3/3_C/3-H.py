
n = 8
Map = [0, 1, 1, 0, 0, 0, 1, 0]
F = [1, 0, 0, 0, 0, 0, 0, 0]
# F = [0] * (n + 1)
# F[0] = 1
# print('F  '+str(F))

# print('Map  '+str(Map))
for i in range(1, n):
    # print('i  '+str(i))
    # print('Map[i]  '+str(Map[i]))
    if Map[i] == 0:
        F[i] = sum(F[max(0, (i - 3)): i])
        # print('max(0, (i - 3) = ' + str(max(0, (i - 3))))
        # print('F[max(0, (i - 3)): i] = ' + str(F[max(0, (i - 3)): i]))
        # print('sum(F[max(0, (i - 3)): i]) = ' +
            #   str(sum(F[max(0, (i - 3)): i])))
        # F[i] = 0
    else:
        F[i] = 0
        # F[i] = sum(F[max(0, (i-3)): i])
# print("F[n]   "+str(F[n-1]))
# print("F   "+str(F))
