import turtle as t
t.speed(0)
t.turtlesize(2,2,2)
def up():
    t.fd(50)
def left():
    t.lt(90)
def right():
    t.rt(90)
t.onkeypress(up,"Up")
t.onkeypress(left,"Left")
t.onkeypress(right,"Right")
t.listen()
t.done()