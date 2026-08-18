import turtle as t
t.speed(0)
t.turtlesize(2,2,2)
t.bgcolor("blue")
t.pencolor("green")
def up():
    t.fd(50)
def left():
    t.lt(15)
def right():
    t.rt(15)
def a(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
def morewidth():
    t.width(t.width()+2)
def lesswidth():
    t.width(t.width()-2)
t.onkeypress(up,"Up")
t.onkeypress(left,"Left")
t.onkeypress(right,"Right")
t.onkeypress(morewidth,">")
t.onkeypress(lesswidth,"<")
t.onscreenclick(a)
t.listen()
t.done()