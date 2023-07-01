import turtle

rama=turtle.Turtle()
turtle.bgcolor("black")
rama.pencolor("red")
rama.speed(0)
#turtle.screensize(canvwidth=2000,canvheight=2000)
def hysteria(steps,move):
    if(steps==0):
        return
    rama.fd(steps)
    rama.rt(90)
    rama.rt(2)
    hysteria(steps-4,move/2)
    
rama.penup()
rama.goto(-100,250)
rama.pendown()

hysteria(600,360)


turtle.done()