import turtle
rama=turtle.Turtle()
turtle.bgcolor("black")
rama.color("yellow","red")

def squarcirc(a):
    c=0
    while True:
        for i in range(0,4):
            rama.fd(a)
            rama.rt(90)
        rama.rt(5)
        c+=1
        if(c==74):
            break

rama.speed(0)

squarcirc(100)
rama.penup()
rama.goto(0,0)
rama.pendown()
rama.pencolor("red")
squarcirc(200)

turtle.done()