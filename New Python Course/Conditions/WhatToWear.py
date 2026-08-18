rainy=input("How's the weather outside? is it raining? (yes/no): ").lower()
cold=input("Is it cold outside? (yes/no): ").lower()
if rainy=="yes" and cold=="yes":
    print("Wear a raincoat and a warm jacket.")
elif rainy=="yes" and cold=="no":
    print("Wear a raincoat.")
elif rainy=="no" and cold=="yes":
    print("Wear a warm jacket.")
elif rainy=="no" and cold=="no":
    print("Wear whatever you like.")
else:
    print("Invalid Input. Please answer with 'yes' or 'no'.")