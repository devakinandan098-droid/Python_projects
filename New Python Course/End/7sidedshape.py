import turtle as t
t.speed(0)
t.bgcolor("black")
colors=["red","blue","orange","white","gray","sky blue","sky blue","green"]
for x in range(100):
    t.pencolor(colors[x%7])
    t.fd(x)
    t.lt(360/7+1)

t.done()