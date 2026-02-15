ns=int(input("enter a number"))
ne=int(input("enter a number"))
sum=0
for i in range(ns,ne+1):
    if(i%2==0):
        sum=sum+i
print(sum)

