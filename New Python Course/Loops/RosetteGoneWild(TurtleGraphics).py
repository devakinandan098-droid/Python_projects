import turtle as t
t.bgcolor("black")
t.width(2)
circles=int(t.numinput("Number of Circles",
                       "How many circles would you like in your rosette?",6))
t.speed(0)
for x in range(circles):
    t.pencolor("red")
    t.circle(100)
    t.pencolor("yellow")
    t.circle(50)
    t.lt(360/circles)
t.done()