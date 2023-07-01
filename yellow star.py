import turtle

rama=turtle.Turtle()
turtle.bgcolor("black")
turtle.title("pushymitra")
rama.color("yellow","red")
rama.fd(200)

def loc(a,b):
    rama.penup()
    rama.fd(a)
    if(b==True):
        rama.lt(90)
    rama.pendown()

def mov():
    for i in range(0,10):
        rama.lt(160)
        rama.fd(200)

mov()
rama.tilt(90)
loc(400,False)
mov()
loc(600,False)
mov()
loc(400,True)
mov()

turtle.done()
