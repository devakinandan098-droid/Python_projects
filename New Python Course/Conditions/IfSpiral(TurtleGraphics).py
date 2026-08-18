answer=input("Do you want to see a spiral?(yes/no): ")
if answer=="yes":
    print("Working...")
    import turtle as t
    t.speed(0)
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
    t.done()
    print("Thank you for using the program. Have a nice day!")

if answer!="yes" or "no":
    print("Invalid input. Please enter 'yes' or 'no'.")