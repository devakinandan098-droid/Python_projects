import turtle as t
t.speed(0)
number=int(t.numinput("Number of sides or Circles","How many sides or circles do you want in your shape?",6))
shape=t.textinput("Which shape do you want?","Enter 'polygon' for a polygon or 'rosette' for a rosette: ")
for x in range(number):
    if shape=="polygon":
        t.forward(150)
        t.left(360/number)
    elif shape=="rosette":
        t.circle(100)
        t.left(360/number)
else:
    print("Invalid input. Please run the program again and enter 'polygon' or 'rosette'.")
t.done()