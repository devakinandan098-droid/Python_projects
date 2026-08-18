# ColorSpiral.py
import turtle as t
t.speed(0)
t.bgcolor("black")
# You can choose between 2 and 6 sides for some cool shapes!
sides=eval(input("Enter how many sides you want(pick from 2-10): "))
colors = ["red", "yellow", "blue", "orange", "green", "purple", "pink", "white", "cyan", "magenta"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
t.done()