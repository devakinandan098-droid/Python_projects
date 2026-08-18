import random as r
import turtle as t
t.speed(0)
t.bgcolor("black")
colors=["red","white","grey","blue","green","sky blue","orange","yellow"]
def random_spiral():
    t.pencolor(r.choice(colors)) 
    size = r.randint(10,40)
    x = r.randrange(-t.window_width()//2,
                         t.window_width()//2)
    y = r.randrange(-t.window_height()//2,
                         t.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for z in range(size):
        t.fd(z*2)
        t.lt(91)
for z in range(50):
    random_spiral()
t.done()