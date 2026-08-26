logo="""
   _____      _            _       _             
  / ____|    | |          | |     | |            
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                 
                                                 
"""
print(logo)
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}
def calculator():
    should_accumalate=True
    num1=float(input("Enter your first number: "))
    while should_accumalate:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Enter your operation: ")
        num2=float(input("Enter your second number: "))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice=input(f"Type 'y' to continue calculating with {answer} or type 'n' to start over")

        if choice == "y":
            num1=answer
        else:
            should_accumalate=False
            print("\n"*20)
            print(logo)
            calculator()
calculator()