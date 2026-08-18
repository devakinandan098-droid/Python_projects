import random as r
import turtle as t
t.speed(0)
t.bgcolor("black")
t.hideturtle()
colors=["red","blue","green","white","gray","sea green","sky blue","orange"]
def a(x,y):
    t.pencolor(r.choice(colors))
    c=r.randint(10,40)
    b(x,y, c)
    b(-x,y, c)
    b(-x,-y, c)
    b(x,-y, c)
def b(x,y, c):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for z in range(c):
        t.fd(z*2)
        t.lt(92)
t.onscreenclick(a)
t.done()