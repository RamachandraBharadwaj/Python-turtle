import turtle
rama=turtle.Turtle()
turtle.bgcolor("black")
rama.color("purple","red")
colors=[]
c=0
while True:
    for i in range(0,20):
        rama.fd(i*10)
        if(i>=10):
            rama.stamp()
        rama.rt(119)
    
    c+=1
    rama.penup()
    if(c<=4):
        rama.fd(600)
    else:
        rama.fd(900)

    rama.pendown()
    if(c==12):
        break
    

turtle.done()