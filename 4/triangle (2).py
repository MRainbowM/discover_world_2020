import math
a = input().split(' ')
b = input().split(' ')
c = input().split(' ')
skalprab = int(a[0])*int(b[0]) + int(a[1])*int(b[1])
skalprac = int(a[0])*int(c[0]) + int(a[1])*int(c[1])
skalprcb = int(b[0])*int(c[0]) + int(b[1])*int(c[1])
lenac = (int(a[0])-int(c[0]))**2 + (int(a[1])-int(c[1]))**2
lenab = (int(b[0])-int(a[0]))**2 + (int(b[1])-int(a[1]))**2
lencb = (int(b[0])-int(b[0]))**2 + (int(b[1])-int(b[1]))**2
maxstor = max(lenac,lenab,lencb)
if (maxstor==lenac):
    cosa=skalprcb/(math.sqrt(lencb)*math.sqrt(lenab))
elif (maxstor==lenab):
    cosa=skalprac/(math.sqrt(lencb)*math.sqrt(lenac))
else:
    cosa=skalprab/(math.sqrt(lenac)*math.sqrt(lenab))
if (cosa>0):
    print("ACUTE")
elif (cosa<0):
    print("OBTUSE")
else:
    print("RIGHT")