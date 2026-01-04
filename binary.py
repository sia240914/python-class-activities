num=int(input("enter your number"))
binary=""
quotient=num
while(quotient>1):
    remainder=quotient%2
    binary=str(remainder)+binary
    quotient=quotient//2
print(binary)