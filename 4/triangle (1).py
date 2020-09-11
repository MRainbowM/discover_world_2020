import math

a = input().split(' ')
b = input().split(' ')
c = input().split(' ')

skalprab = int(a[0])*int(b[0]) + int(a[1])*int(b[1])
skalprac = int(a[0])*int(c[0]) + int(a[1])*int(c[1])
skalprcb = int(b[0])*int(c[0]) + int(b[1])*int(c[1])

lena = (int(c[0])-int(b[0]))**2 + (int(c[1])-int(b[1]))**2
lenb = (int(c[0])-int(a[0]))**2 + (int(c[1])-int(a[1]))**2
lenc = (int(b[0])-int(a[0]))**2 + (int(b[1])-int(a[1]))**2
maxstor = max(lena, lenb, lenc)
if (maxstor == lena):
    cosa = skalprcb/(math.sqrt(lenc)*math.sqrt(lenb))
elif (maxstor == lenb):
    cosa = skalprac/(math.sqrt(lenc)*math.sqrt(lena))
else:
    cosa = skalprab/(math.sqrt(lena)*math.sqrt(lenb))
if (cosa > 0):
    print("ACUTE")
elif (cosa < 0):
    print("OBTUSE")
else:
    print("RIGHT")
