import turtle as t
t.bgcolor("black")
t.speed(0)
colors=["red","blue","yellow","green"]
for x in range(400):
    t.pencolor(colors[x%4])
    t.fd(x)
    t.lt(91)
t.done()