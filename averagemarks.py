maths=int(input("enter your math marks"))
english=int(input("enter your english marks"))
SS=int(input("enter your SS marks"))
hindi=int(input("enter your hindi marks"))
marathi=int(input("enter your marathi marks"))
total=maths+english+SS+hindi+marathi
average=total/5

if(average>=91 and average<=100):
    print("A grade")
elif (average>=81 and average<=90):
    print("B grade")
elif (average>=71 and average<=80):
    print("C grade")
elif (average>=61 and average<=70):
    print("D grade")
elif (average>=51 and average<=60):
    print("E grade")
else:
    print("fail")