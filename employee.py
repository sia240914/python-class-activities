class employee :
    def __init__(self):
        print("constructor is called over here ")

    def __del__(self):
        print("destructor called")

def createobj():
    print("making the object")
    e1=employee()
    return e1 
obj=createobj()
