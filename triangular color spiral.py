import turtle

rama=turtle.Turtle()
turtle.bgcolor("black")
rama.color("blue")
turtle.speed(10)
colorsu=["red","yellow","green","purple","blue","pink","orange","light green"]

for i in range(600):
    rama.fd(i*5)
    rama.lt(119)
    try:
        x=i%10
        rama.pencolor(colorsu[x])
    except:
        rama.pencolor("indigo")


turtle.done()
