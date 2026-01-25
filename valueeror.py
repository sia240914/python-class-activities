try:
    num=int(input("enter your number:"))
    print("you entered:",num)

except ValueError as e:
    print(e)

