import turtle as t
t.speed(0)
t.bgcolor("black")
colors=["red","blue","yellow","green","orange","purple","white","gray","brown","sea green"]
name=t.textinput("Enter you name","What is Your Name?")
sides=int(t.numinput("Number of sides",
                     "How many sides do you want?(1-10)?",5,1,10))
for x in range(100):
    t.pencolor(colors[x%sides%10])
    t.penup()
    t.fd(x*4)
    t.pendown()
    t.write(name,font=("Black Ops 1",int((x*2+4)/4),"bold"))
    t.lt(360/sides+2)
t.done()