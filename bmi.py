height=float(input("enter your height in cm"))
weight=float(input("enter your weight in kg"))
bmi=weight/(height/100 )**2
print ("the  bmi is : ",bmi)

if bmi<=18.4:
    print ("underweight")
elif bmi<=24.9 :
    print ("healthy")
elif bmi<=29.9 :
    print ("overweight")
elif bmi<=34.9 :
    print ("severly overweight")
elif bmi<=39.9 :
    print ("obese")
else :
    print("severly over obese")