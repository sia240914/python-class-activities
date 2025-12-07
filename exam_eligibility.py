attendance=int(input("enter the attendance"))

if(attendance>=75):
    print("your allowed to sit for the exam")
else:
    medical_reason=(input("is there a medical reason?(Y/N)"))
    if(medical_reason=='Y'):
        print("your allowed to sit for the exam")
    elif(medical_reason=='N'):
        print("you cannot sit for the exam")
    