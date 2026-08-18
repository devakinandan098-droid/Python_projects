import turtle as t
t.penup()
t.speed(0)
t.bgcolor("black")
sides = int(t.numinput("Number of sides",
            "How many sides in your spiral of rosettes? (2-6)", 4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for m in range(100):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    t.width(m/20)
    for n in range(sides):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.circle(m/5)
        t.right(360/sides)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)
t.done()