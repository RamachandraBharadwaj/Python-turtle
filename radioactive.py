import turtle
def lupo(n):
    for i in range(0,n):
        rama.fd(200)
        rama.stamp()
        rama.lt(120)

rama=turtle.Turtle()
turtle.bgcolor("black")
rama.color("red","yellow")
rama.ht()

rama.begin_fill()
lupo(5)

rama.fd(300)
lupo(3)

rama.rt(120)
rama.fd(100)
lupo(3)

rama.end_fill()

turtle.done()