import turtle

rama=turtle.Turtle()
turtle.bgcolor("black")
rama.color("blue")
turtle.speed(10)
colorsu=["red","yellow","green","purple","blue","pink","orange","light green","red","#07faf6","#62f202","#f26602","#f20296"]
c=0
rama.speed(0)
for i in range(600):
    rama.fd(i*5)
    rama.lt(119)
    if(i%20==0 and c!=12):
        c+=1
        rama.pencolor(colorsu[c])
    if(c>11):
        c=0
    #try:
        #x=i%10
        #rama.pencolor(colorsu[x])
    #except:
        #rama.pencolor("indigo")


turtle.done()
