import turtle
rama=turtle.Turtle()
turtle.bgcolor("black")
rama.pencolor("yellow")
rama.turtlesize(1)
rama.color("red","yellow")
rama.speed(5)

def circ():
    rama.pendown()
    for i in range(0,10):
        rama.circle(i*10)
        if(i%2==0):
            rama.shape("square")
        else:
            rama.shape("triangle")
    rama.penup()

circ()
rama.fd(400)
circ()
rama.rt(90)
rama.fd(250)
circ()
rama.rt(90)
rama.fd(400)
circ()





turtle.done()
