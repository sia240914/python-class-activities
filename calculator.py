def add (num1,num2):
    return num1+num2
def sub (num1,num2):
    return num1-num2
def mul (num1,num2):
    return num1*num2
def div (num1,num2):
    return num1/num2
num1=float(input("enter the number"))
num2=float(input("enter the number"))
operation=input("enter the operater(+,-,*,/)")
if operation=='+':
    print(add(num1,num2))
if operation=='-':
        print(sub(num1,num2))
if operation=='*':
    print(mul(num1,num2))
if operation=='/':
    print(div(num1,num2))
