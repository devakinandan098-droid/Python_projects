import turtle as t
t.speed(0)
t.bgcolor("black")
colors=["red","yellow","blue","green","orange","purple","white","brown","gray","pink",]
family=[]
name=t.textinput("My family",
                 "Enter a name, or just hit [Enter] top end: ")
while name != "" :
    family.append(name)
    name=t.textinput("My family",
                 "Enter a name, or just hit [Enter] top end: ")
for x in range(100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)],font=("Arial", int((x+4)/4) , "bold"))
    t.lt(360/len(family)+2)
t.done()
