valid=False
while not valid:
    try:
        n=int(input("enter your number:"))
        while n%2==0:
            print ("bye")
        valid=True
    except ValueError as e :
        print(e)

        