rowsize=8
halfrowsize=0
if (rowsize%2==0):
    halfrowsize=int(rowsize/2)
else:
    halfrowsize=int(rowsize/2)+1

space=halfrowsize-1
for i in range (1,halfrowsize+1):
    for j in range (1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range (2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1

for i in range (1,halfrowsize):
    for j in range (1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range (1,2*(halfrowsize-i)):
        print(end=str(num))
        num=num+1
    print()