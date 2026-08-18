import turtle as t
t.speed(0)
t.bgcolor("black")
colors = ["red","yellow","blue","green","purple","orange","gray","white"]
sides=int(t.numinput("Number of sides",
                     "How many sides do you want (1-8)?",4,1,8))
your_name=t.textinput("Enter your name","What is your name?")
for x in range(360):
    t.pencolor(colors[x%sides])
    t.fd(x*3/sides+x)
    t.lt(360/sides+1)
    t.write(your_name,font=("Impact",int((x+4)/4),"bold"))
    t.width(x*sides/200)
t.done()