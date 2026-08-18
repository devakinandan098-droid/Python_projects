import turtle as t
import random as r
t.speed(0)
t.bgcolor("black")
colors=["red","""blue""","white","gray","green","orange","yellow","sky blue"]
for z in range(50):
    t.pencolor(r.choice(colors))
    size=r.randint(10,40)
    x=r.randrange(0,t.window_width()//2)
    y=r.randrange(0,t.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for q in range(size):
        t.fd(q*2)
        t.lt(91)
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for q in range(size):
        t.fd(q*2)
        t.lt(91)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for q in range(size):
        t.fd(q*2)
        t.lt(91)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for q in range(size):
        t.fd(q*2)
        t.lt(91)
t.done()