import turtle as t
t.bgcolor("black")
t.speed(0)
Colors = ["red","blue","green","yellow"]
for x in range(100):
    t.pencolor(Colors[x%4])
    t.circle(x)
    t.lt(91)
