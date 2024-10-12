from turtle import *
from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title('Graphics Demos/Tests')
canva=Canvas(root)
canva.config(width=800,height=600)
canva.pack()
board=TurtleScreen(canva)
drawer=RawTurtle(board)

#Functions:
def clearsrc():
    board.reset()
def drawsquare():
    for i in range(0,4):
        drawer.fd(100)
        drawer.rt(90)

def drawtriangle():
    for i in range(0,3):
        drawer.lt(120)
        drawer.fd(100)


def drawrectangle():
    for i in range(0,2):
        drawer.fd(150)
        drawer.lt(90)
        drawer.fd(100)
        drawer.lt(90)

def drawhexagon():
    drawer.lt(180)
    for i in range(0,6):
        drawer.fd(100)
        drawer.rt(60)

def drawparallelogram():
    for i in range(0,4):
        drawer.fd(150)
        drawer.rt(60)
        drawer.fd(100)
        drawer.rt(120)

def drawoctagon():
    for i in range(0,8):
        drawer.fd(100)
        drawer.rt(45)

menuar=Menu()
menu_func=Menu(tearoff=0)
menu_func.add_command(
    label='Square',
    command=drawsquare
)
menu_func.add_command(
    label='Triangle',
    command=drawtriangle
)
menu_func.add_command(
    label='Rectangle',
    command=drawrectangle
)
menu_func.add_command(
    label='Hexagon',
    command=drawhexagon
)
menu_func.add_command(
    label='Parallelogram',
    command=drawparallelogram
)
menu_func.add_command(
    label='Octagon',
    command=drawoctagon
)
menu_func.add_command(
    label='Reset Canvas',
    command=clearsrc
)

menuar.add_cascade(menu=menu_func,label='Demos')
root.config(width=640,height=480,menu=menuar)

# def forwd():
#     drawer.fd(25)
# def loft():
#     drawer.lt(10)

# onkeypress(forwd,'Up')
# onkeypress(loft,'Left')
# listen()
mainloop()