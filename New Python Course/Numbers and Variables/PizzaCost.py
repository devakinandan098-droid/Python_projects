number_of_pizzas = eval(input("Enter the number of pizzas you would like:" ))
cost_per_pizza = eval(input("Enter the cost per pizza: "))
subtotal=number_of_pizzas*cost_per_pizza
tax_rate=0.08
sales_tax=subtotal*tax_rate
Total=tax_rate+subtotal

print("Your total is $",Total)
print("This includes $",subtotal,"for the pizza and $",sales_tax,"for the tax")
print("Thank you for shopping here today")
print("Have a good morning!")