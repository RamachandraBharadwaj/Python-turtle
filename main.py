from subprocess import call 
import tkinter
import os

os.chdir(r"E:\\Coding guide\\my python\\turtle files")
def cretwin():
    errpop=tkinter.Toplevel(rama)
    errpop.title("waitt!!")
    icon=tkinter.PhotoImage(file="maoi.png")
    errpop.iconphoto(True,icon)
    errpop.resizable(0,0)
    cat=tkinter.PhotoImage("broo.png")
    partu=tkinter.Label(errpop,text="please follow the instructions \n enter from the given number options",font=("Comic sans",24),padx=50,pady=25,fg="blue",bg="yellow",relief="raised",image=icon,compound="bottom")
    partu.pack()


def accept():
    s=inpu.get()
    match s:
        case "1":
            call(["Python3","radioactive.py"])
        case '2':
            call(["Python3","circle with squares.py"])
        case "3":
            call(["Python3","concentric circles.py"])
        case "4":
            call(["Python3","multiple triangular spiral.py"])
        case "5":
            call(["Python3","yellow star.py"])
        case "6":
            call(["Python3","square spiral.py"])
        case "7":
            call(["Python3","triangular color spiral.py"])
        case _:
            cretwin()
            print("bruh.mp3")

rama=tkinter.Tk()
rama.geometry("720x720")
rama.title("Main menu - polygons")
rama.config(background="black")


thumbnail=tkinter.PhotoImage(file="dixie.png")
mm=tkinter.PhotoImage(file="gui menu0000.png") #720 x 720 width height
rama.iconphoto(True,thumbnail)
label=tkinter.Label(image=mm, relief="raised")
label.pack()



inpu=tkinter.Entry(rama,font=("Comic sans",22),width=41)
inpu.place(x=290,y=710)


enterbutton=tkinter.Button(rama,text="let's go!",font=("Arial",12),command=accept,compound="bottom",padx=5,pady=5)
enterbutton.place(x=938,y=710)


rama.mainloop()