import random
user=input("enter your choice : r p s ")
computer=random.choice(["r","p","s"])
print ("your choice is :", user)
print("computer choice is ",computer)
if computer==user:
    print("its a tie")

elif user=="r":
    if computer=="p":
        print("you lose")
    elif computer=="s":
        print("you win")

elif user=="p":
    if computer=="r":
        print("you win")
    elif computer=="s":
        print("you lose")

elif user=="s":
    if computer=="r":
        print("you lose")
    elif computer=="p":
        print("you win")
