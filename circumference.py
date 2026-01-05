
import math

def circumference_of_circle(r):
    return 2* math.pi * r
radius = float(input("Enter the radius of the circle: "))
circumference = circumference_of_circle(radius)
print("the circumference of the circle is :", circumference)
