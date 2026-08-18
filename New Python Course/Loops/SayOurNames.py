name=input("Please enter your name: ")
while name !="":
    for x in range(100):
        print(name,end=" ")
    print()
    name=input("Enter another name, or just hit [Enter] to quit: ")
print("Thanks for playing!")