import turtle as t
t.speed(0)
t.bgcolor("black")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for x in range(4):
    t.penup()
    t.rt(180)
    t.fd(600)
    t.lt(180)
    t.pendown()
    for x in range(4):
        for x in range(3):
            t.color(colors[x % 7])
            t.penup()
            t.fd(100)
            t.pendown()
            for x in range(3):
                t.fd(100)
                t.lt(120)
    t.penup()
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(900)
    t.pendown()
    t.fd(600)
    t.lt(180)
    for x in range(4):
        for x in range(3):
            t.color(colors[x % 7])
            t.penup()
            t.fd(50)
            t.pendown()
            for x in range(3):
                t.fd(100)
                t.lt(120)
t.done()