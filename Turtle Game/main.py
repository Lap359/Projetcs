from turtle import *
from math import *
from random import *
from time import *
from playsound import *
root=Screen()
root.bgcolor('gray')
# root.bgpic('assets/bg.gif')
enemyspeed = 2
bulletstate_quaivat="ready"
#Setup some bullets:
bullet=Turtle()
bullet.color('yellow')
bullet.shape('arrow')
bullet.penup()
bullet.seth(0)
bullet.hideturtle()
bulletstate='ready'
#Setup guns:)
gun=Turtle()
gun.color("red")
gun.shape("circle")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(0.5, 0.5)
gun.hideturtle()
#Setup stopwatch:
value=time()
def stpwtch(value):
    valued=(((value/365)/24)/60)
    days=int(valued)
    valueh=(valued-days)*365
    hours=int(valueh)
    valuem=(valueh-hours)*24
    minutes=int(valuem)
    values=(valuem-minutes)*60
    return int(values)
#Dra the Times:
time_pen=Turtle()
time_pen.speed(0)
time_pen.color('gray')
time_pen.penup()
time_pen.setpos(-20,260)
end_s=time()
s=stpwtch(end_s-value)
timestr=str(s)
time_pen.write(timestr,False,align="left",font=("Times New Roman",14,"normal"))
time_pen.hideturtle()
#Draw scores:
score=0
score_pen=Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setpos(-290,280)
scorestr="Player: %s" %score
score_pen.write(scorestr,False,align="left",font=("Times New Roman",14,"normal"))
score_pen.hideturtle()
#Draw opposite scores:
score=0
score_pen_qv=Turtle()
score_pen_qv.speed(0)
score_pen_qv.color('white')
score_pen_qv.penup()
score_pen_qv.setpos(290,280)
scoreqvstr="Enemy: %s" %score
score_pen_qv.write(scorestr,False,align="left",font=("Times New Roman",14,"normal"))
score_pen_qv.hideturtle()
#Setup You:
payer=Turtle()
payer.penup()
payer.shape('turtle')
#Setup some jerk:
enemy=Turtle()
# image='assets/dog.gif'
# root.addshape(image)
enemy.shape('triangle')
enemy.penup()
enemy.setpos(randint(-300,300),randint(-300,300))
#Controls Setup:
speed=1
def trnlt():
    payer.lt(10)
def trnrt():
    payer.rt(10)
def icrsespd():
    global speed
    speed+=1
    if speed>=5:
        speed=1
    payer.fd(speed)
def dcrsespd():
    global speed
    speed-=1
    if speed<=-5:
        speed=-5
    payer.fd(speed)
#Collision Checking
def iscollided(t1,t2):
    d=sqrt(pow(t1.xcor()-t2.xcor(),2)+pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
def boundarychecking(t):
    if t.xcor() < -300 or t.xcor() > 300:
        t.rt(180)
        t.setposition(randint(-300,300),randint(-300,300))
    else:
        t.lt(180)
        t.setposition(randint(-300,300),randint(-300,300))
#KeyMappings
root.listen()
onkey(icrsespd,'Up')
onkey(dcrsespd,'Down')
onkey(trnrt,'Right')
onkey(trnlt,'Left')

def fire_in_the_hole():
	global bulletstate
	if bulletstate=='ready':
		bulletstate='fire'
		x=payer.xcor()
        y=payer.ycor()+10
        gun.setpos(x,y)
        gun.showturtle()
    
def fire_in_the_hole2():
	global bulletstate_enemy
	if bulletstate_enemy=='ready':
		bulletstate_enemy='fire'
		x=enemy.xcor()
        y=enemy.ycor()+10
        gun.setpos(x,y)
        gun.showturtle()

while True:
    end_s=time()
    s=stpwtch(s-value)
    timestr=str(s)
    time_pen.clear()
    time_pen.write(timestr,False,align='left',font=('Times New Roman',14,'normal'))
    time_pen.hideturtle()

    x=enemy.xcor()
    x+=enemyspeed
    enemy.setx(x)

    fire_in_the_hole2()
    

    boundarychecking(payer)
    if iscollided(payer,enemy):
        print("Done")
        break
    enemy.fd(10)
    enemy.rt(randint(10,100))
    boundarychecking(enemy)
root.mainloop()
