import turtle

rama=turtle.Turtle()
rama.color("red","yellow")
rama.begin_fill()
for i in range(0,4):
    rama.forward(100)
    rama.left(90)


rama.penup()
rama.forward(200)

for i in range(0,4):
    rama.forward(100)
    rama.left(90)

rama.end_fill()

turtle.done()