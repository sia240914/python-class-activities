from abc import ABC , abstractmethod

class TASK (ABC):
    def printvalue(self,x):
        print ("this is x :",x)
    @abstractmethod
    def task (self):
        print ("i am inside a Task_class")
class test(TASK):
    def task(self):
        print("i am in test class ")
t1=test()
t1.task()
t1.printvalue(1000000)

    