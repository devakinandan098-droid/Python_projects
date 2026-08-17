import turtle as t
import colorsys as c
t.speed(0)
t.bgcolor("black")
t.hideturtle()
t.colormode(1.0)
hue=0.0
for x in range(36):
    for z in range(12):
        t.pencolor(c.hsv_to_rgb(hue,1,1))
        t.fd(100)
        t.lt(30)
        hue+=0.01
    t.lt(10)
t.done()