import turtle
turtle.Screen().bgcolor("dark blue")
screen = turtle.Screen()
screen.setup(width=400,height=400)
square = turtle.Turtle()
sides = 4
angle = 360 / sides
for i in range (sides):
    square.forward(100)
    square.right(90)