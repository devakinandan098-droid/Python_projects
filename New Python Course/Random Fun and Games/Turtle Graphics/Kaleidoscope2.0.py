import turtle as t
import random as r
t.speed(0)
t.bgcolor("black")
colors=["red","blue","white","gray","green","orange","yellow","sky blue"]

for n in range(50):
    sides=r.randint(3,9)
    size=r.randint(10,40)
    wide=r.randint(1,5)
    t.pencolor(r.choice(colors))
    x=r.randrange(0,t.window_width()//2)
    y=r.randrange(0,t.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for q in range(size):
        t.width(wide)
        t.fd(q*2)
        t.lt((360/sides)+1)
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for q in range(size):
        t.width(wide)
        t.fd(q*2)
        t.lt((360/sides)+1)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for q in range(size):
        t.width(wide)
        t.fd(q*2)
        t.lt((360/sides)+1)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for q in range(size):
        t.width(wide)
        t.fd(q*2)
        t.lt((360/sides)+1)
t.done()