import random
playing=True
number=random.randint(1,20)
print("guess the number from 1,20")
while playing:
    guess=int(input("enter the number : "))
    if guess==number:
        print("you guessed the right number")
        break
    else:
        print("try again")