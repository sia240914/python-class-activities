num1=int(input("enter your number 1 "))
num2=int(input("enter your number 2 "))
num3=int(input("enter your number 3 "))
temp=0
print(num1, num2, num3)   
temp=num1
num1=num3
num3=num2
num2=temp
print(num1, num2, num3)