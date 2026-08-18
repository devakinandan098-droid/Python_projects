import random
import turtle as t
t.speed(0)
t.bgcolor("black")
t.hideturtle()
colors = ["red", "yellow", "blue", "green", "orange", "purple", 
          "white", "gray"]
for n in range(100):
    t.pencolor(random.choice(colors))   # Pick a random color 
    size = random.randint(10,40)
    x = random.randrange(-t.window_width()//2,
                         t.window_width()//2)
    y = random.randrange(-t.window_height()//2,
                         t.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(61)

t.done()