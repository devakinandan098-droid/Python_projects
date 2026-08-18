driving=eval(input("Enter the legal driving age where you live: "))
age=eval(input("Enter your age: "))
if age>=driving:
    print("You are old enough to drive.")
else:
    print("Sorry, you can drive in", driving-age, "years.")