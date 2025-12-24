import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
size=0
while True:
    for i in range(4):
        polygon.forward(size+1)
        polygon.right(90)
        size=size-5
    size=size+1
