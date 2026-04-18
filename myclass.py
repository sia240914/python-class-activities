class myclass :
    __privatevar=472
    def __privatemethord(self):
        print("i am inside  my class")
    
    def hello(self):
        print("private variable is ", myclass.__privatevar)
        self.__privatemethord()
obj=myclass()

obj.hello()