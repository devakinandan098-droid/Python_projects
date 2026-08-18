import random as r
import turtle as t
t.bgcolor('black')
colors=['red', 'sea green', 'blue', 'green', 'orange',
        'sky blue', 'white', 'gray']
def a(x,y):
    t.speed(0)
    t.hideturtle()
    color1 = r.choice(colors)
    color2 = r.choice(colors) 
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.width(r.randint(1,5))
    size = r.randint(6,24)
    t.pencolor(color1)
    for z in range(size//2):
        t.circle(size)
        t.left(360/size*2)
    t.pencolor(color2)
    for z in range(size//2):
        t.circle(size/3)
        t.left(360/size*2)
t.onscreenclick(a)
t.done()