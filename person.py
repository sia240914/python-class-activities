class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def desplay (self):
        print(self.name)
        print(self.idnumber)

class employee (person):
    def __init__(self ,name ,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
    
    def desplay(self):
        super().desplay()
        print(self.salary)
        print(self.post)
e1=employee("sia",23897,10000000,"software engg")
e1.desplay()