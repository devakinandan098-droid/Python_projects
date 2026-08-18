import turtle as t
import colorsys as c
t.speed(0)  
t.bgcolor("black")
t.hideturtle()
t.width(3)
circles=int(t.numinput("Number of Circle","How many circles would you like in your rosette?"))
for z in range(circles):
    t.pencolor(c.hsv_to_rgb(z/circles,1,1))
    t.circle(150)
    t.lt(360/circles)
t.done()