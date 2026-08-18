import turtle as t
t.bgcolor("black")
t.speed(0)
colors=["red","blue","yellow","green"]
your_name=t.textinput("Enter your name","What is your name?")
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.fd(x*4)
    t.pendown()
    t.write(your_name,font=("Impact",int((x+4)/4),"bold"))
    t.lt(92)
t.done()