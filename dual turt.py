import turtle
rama=turtle.Turtle()
bharadwaj=turtle.Turtle()
turtle.bgcolor("black")
rama.pencolor("red")
bharadwaj.pencolor("magenta")

def symetro(x,c,d):
    x.hideturtle()
    x.begin_fill()
    x.color(d)

    for i in range(0,10):
        if(c%2==0):
            x.fd(100)
            x.rt(20)
        else:
            x.back(100)
            x.lt(20)

    x.end_fill()

rama.penup()
rama.goto(0,250)
bharadwaj.penup()
bharadwaj.goto(0,250)
rama.pendown()
bharadwaj.pendown()
symetro(rama,1,"red")
symetro(bharadwaj,2,"yellow")












turtle.done()