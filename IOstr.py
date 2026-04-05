class IOstr:
    def __init__(self):
        self.str1=""
    def inputstr(self):
        self.str1=input("enter a string:")
    def outputstr(self):
        print(self.str1.upper())



str1=IOstr()

str1.inputstr()
str1.outputstr()