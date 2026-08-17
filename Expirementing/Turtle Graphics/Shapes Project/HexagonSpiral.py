import turtle as t
t.bgcolor("black")
y=int(t.numinput("Input", "How many flashes would you like(20-100)?"))
i=3
t.speed(0)
color = ["red", "blue", "green"]
t.penup()
t.rt(90)
t.fd(200)
t.lt(90)
t.fd(100)
t.pendown()
for x in range(6):
    t.color(color[x % 3])
    for x in range(6):
        t.lt(10)
        t.lt(60)
        t.fd(100)
    for x in range(2):
        t.color(color[x % 3])
        for x in range(6):
            t.lt(10)
            t.lt(60)
            t.fd(100)
    t.penup()
    t.fd(200)
    t.lt(60)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    t.pendown()
    for x in range(2):
        t.color(color[x % 3])
    for x in range(6):
        t.lt(10)
        t.lt(60)
        t.fd(100)
t.penup()
t.lt(90)
t.fd(100)
t.fd(150)
t.pendown()
t.hideturtle()
t.speed(0)
for i in range(y):
    if i%2==0:
        t.bgcolor("white")
    else:
        t.bgcolor("black")
    c=color[i%len(color)]
    t.pencolor(c)
    t.fillcolor(c)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
t.done()

#DO NOT edit project