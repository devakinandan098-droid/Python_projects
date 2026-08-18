driving=eval(input("Enter the legal driving age where you live: "))
age=eval(input("Enter your age: "))
if age>=driving:
    print("You are old enough to drive.")
if age<driving:
    print("Sorry, you can drive in", driving-age, "years.")

if age==15 and driving==15:
    print("You can drive with a learner's permit.")