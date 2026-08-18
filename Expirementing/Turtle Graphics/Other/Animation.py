import turtle as t
import random as r
t.hideturtle()
t.bgcolor("black")
t.speed(0)
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
for x in range(r.randint(100,1000)):
    t.pencolor(colors[x % len(colors)])
    for y in range(6):
        t.lt(100)
        t.fd(100)
        t.rt(60)

t.done()