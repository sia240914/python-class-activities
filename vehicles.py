class vehicles:
    def __init__(self,name,max_speed,capacity):
        self.name=name
        self.max_speed=max_speed
        self.capacity=capacity
class car (vehicles):
    print(" this is the child class car")

c1 =car("honda",100,5)