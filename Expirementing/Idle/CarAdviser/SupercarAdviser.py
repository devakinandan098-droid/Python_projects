logo = """
     _______. __    __  .______    _______ .______        ______     ___      .______              ___       _______  ____    ____  __       _______. _______ .______      
    /       ||  |  |  | |   _  \  |   ____||   _  \      /      |   /   \     |   _  \            /   \     |       \ \   \  /   / |  |     /       ||   ____||   _  \     
   |   (----`|  |  |  | |  |_)  | |  |__   |  |_)  |    |  ,----'  /  ^  \    |  |_)  |          /  ^  \    |  .--.  | \   \/   /  |  |    |   (----`|  |__   |  |_)  |    
    \   \    |  |  |  | |   ___/  |   __|  |      /     |  |      /  /_\  \   |      /          /  /_\  \   |  |  |  |  \      /   |  |     \   \    |   __|  |      /     
.----)   |   |  `--'  | |  |      |  |____ |  |\  \----.|  `----./  _____  \  |  |\  \----.    /  _____  \  |  '--'  |   \    /    |  | .----)   |   |  |____ |  |\  \----.
|_______/     \______/  | _|      |_______|| _| `._____| \______/__/     \__\ | _| `._____|   /__/     \__\ |_______/     \__/     |__| |_______/    |_______|| _| `._____|
By: Devakinandan Eswar Kalimisetty                                                                                                                                                                         """
supercars = {
    "1": {
        "luxury": {
            "Aston Martin": {"Brand": "Aston Martin", "model": "DB11 V8", "price": "$120,000 - $160,000"},
            "Bentley": {"Brand": "Bentley", "model": "Continental GT", "price": "$160,000 - $220,000"}, 
            "Rolls-Royce": [
                {"Brand": "Rolls-Royce", "model": "Ghost (Gen 1)", "price": "$170,000 - $230,000"},
                {"Brand": "Rolls-Royce", "model": "Wraith", "price": "$220,000 - $320,000"}
            ]
        },
        "sports": {
            "Jaguar": {"Brand": "Jaguar", "model": "F-Type SVR", "price": "$65,000 - $85,000"},
            "Chevrolet": {"Brand": "Chevrolet", "model": "Corvette Z06 (C8)", "price": "$110,000 - $140,000"},
            "Acura": {"Brand": "Acura", "model": "NSX (Second Gen)", "price": "$130,000 - $160,000"},
            "Audi": {"Brand": "Audi", "model": "R8 V10 Plus", "price": "$130,000 - $180,000"},
            "Aston Martin": {"Brand": "Aston Martin", "model": "Vantage V12", "price": "$140,000 - $190,000"},
            "Nissan": {"Brand": "Nissan", "model": "GT-R Nismo", "price": "$160,000 - $210,000"},
            "Lamborghini": {"Brand": "Lamborghini", "model": "Huracán LP 610-4", "price": "$180,000 - $240,000"},
            "Ferrari": {"Brand": "Ferrari", "model": "458 Italia", "price": "$200,000 - $280,000"},
            "Porsche": {"Brand": "Porsche", "model": "911 GT3 RS (991.2)", "price": "$210,000 - $270,000"},
            "McLaren": {"Brand": "McLaren", "model": "720S", "price": "$220,000 - $290,000"}
        }
    },
    "2": {
        "luxury": {
            "Rolls-Royce": [
                {"Brand": "Rolls-Royce", "model": "Dawn", "price": "$280,000 - $380,000"},
                {"Brand": "Rolls-Royce", "model": "Cullinan", "price": "$350,000 - $480,000"},
                {"Brand": "Rolls-Royce", "model": "Phantom VIII", "price": "$450,000 - $600,000"}
            ],
            "Bentley": {"Brand": "Bentley", "model": "Mulsanne Speed", "price": "$290,000 - $350,000"}
        },
        "sports": {
            "Mercedes-AMG": {"Brand": "Mercedes-AMG", "model": "GT Black Series", "price": "$320,000 - $400,000"},
            "Lamborghini": {"Brand": "Lamborghini", "model": "Aventador SVJ", "price": "$650,000 - $800,000"},
            "Ford": {"Brand": "Ford", "model": "GT (Second Gen)", "price": "$750,000 - $900,000"}
        }
    },
    "3": {
        "luxury": {
            "Bugatti": [
                {"Brand": "Bugatti", "model": "Veyron 16.4 Grand Sport", "price": "$1,800,000 - $2,200,000"},
                {"Brand": "Bugatti", "model": "Chiron", "price": "$3,000,000 - $3,800,000"}
            ],
            "Pagani": {"Brand": "Pagani", "model": "Huayra Roadster", "price": "$2,800,000 - $3,600,000"},
            "Rolls-Royce": {"Brand": "Rolls-Royce", "model": "Boat Tail", "price": "$25,000,000 - $28,000,000+"}
        },
        "sports": {
            "Porsche": {"Brand": "Porsche", "model": "Carrera GT", "price": "$1,200,000 - $1,500,000"},
            "McLaren": {"Brand": "McLaren", "model": "P1", "price": "$1,300,000 - $1,700,000"},
            "Ferrari": {"Brand": "Ferrari", "model": "LaFerrari", "price": "$3,200,000 - $4,000,000"},
            "Koenigsegg": {"Brand": "Koenigsegg", "model": "Agera RS", "price": "$4,000,000 - $5,500,000"},
            "Bugatti": {"Brand": "Bugatti", "model": "Chiron Super Sport 300+", "price": "$4,500,000 - $5,500,000"}
            
        }
    }
}
def car_adviser():
    print(logo)
    print("Welcome to the Supercar Adviser!")
    budget = input("Please enter your budget (e.g., 'under 250k(Enter 1)', '250k to 1m(Enter 2)', 'over 1m(Enter 3)'): ").strip().lower()
    if budget not in supercars:
        print("Invalid budget range. Please choose from 'under 250k', '250k to 1m', or 'over 1m'. Please run again.")
    if budget == "1":
        category = input("Do you prefer 'luxury' or 'sports' cars? ").strip().lower()
        if category not in supercars[budget]:
            print("Invalid category. Please choose 'luxury' or 'sports'. Please run again.")
        elif category == "luxury":
            print("Here are some luxury cars within your budget:")
            print(supercars["1"]["luxury"]["Aston Martin"])
            print("\n")
            print(supercars["1"]["luxury"]["Bentley"])
            print("\n")
            print(supercars["1"]["luxury"]["Rolls-Royce"][0])
            print("\n")
            print(supercars["1"]["luxury"]["Rolls-Royce"][1])
            print("\n")
            selected_brand = input("Which brand would you like (Type the brand name)? ").strip().lower()
            if selected_brand == "aston martin":
                print("Your recommended car is:")
                print(supercars["1"]["luxury"]["Aston Martin"][0])
            elif selected_brand == "bentley":
                print("Your recommended car is:")
                print(supercars["1"]["luxury"]["Bentley"])
            elif selected_brand == "rolls-royce":
                print("Your recommended car is:")
                print(supercars["1"]["luxury"]["Rolls-Royce"][0])
                print("or")
                print(supercars["1"]["luxury"]["Rolls-Royce"][1])
            else:
                print("Invalid brand selection.")
        elif category == "sports":
            print("Here are some sports cars within your budget:")
            print(supercars["1"]["sports"]["Jaguar"])
            print("\n")
            print(supercars["1"]["sports"]["Chevrolet"])
            print("\n")
            print(supercars["1"]["sports"]["Acura"])
            print("\n")
            print(supercars["1"]["sports"]["Aston Martin"])
            print("\n")
            print(supercars["1"]["sports"]["Audi"])
            print("\n")
            print(supercars["1"]["sports"]["Nissan"])
            print("\n")
            print(supercars["1"]["sports"]["Lamborghini"])
            print("\n")
            print(supercars["1"]["sports"]["Ferrari"])
            print("\n")
            print(supercars["1"]["sports"]["Porsche"])
            print("\n")
            print(supercars["1"]["sports"]["McLaren"])
            selected_brand = input("Which brand would you like (Type the brand name)? ").strip().lower()
            print("Here is the most recommended car for you:")
            if selected_brand == "jaguar":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "chevrolet":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "acura":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "audi":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "aston martin":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "nissan":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "lamborghini":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "ferrari":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "porsche":
                print(supercars["1"]["sports"][selected_brand.title()])
            elif selected_brand == "mclaren":
                print(supercars["1"]["sports"][selected_brand.title()])
            else:
                print("Invalid brand selection.")
    elif budget == "2":
        category = input("Do you prefer 'luxury' or 'sports' cars? ").strip().lower()
        if category not in supercars[budget]:
            print("Invalid category. Please choose 'luxury' or 'sports'. Please run again.")
        elif category == "luxury":
            print("Here are some luxury cars within your budget:")
            print(supercars["2"]["luxury"]["Rolls-Royce"][0])
            print("\n")
            print(supercars["2"]["luxury"]["Rolls-Royce"][1])
            print("\n")
            print(supercars["2"]["luxury"]["Rolls-Royce"][2])
            selected_brand = input("Which model would you like (Type 1 for the first option, 2 for the second option and 3 for the third option)? ").lower().strip()
            if selected_brand == "1":
                print("Here is the most recommended car for you:")
                print(supercars["2"]["luxury"]["Rolls-Royce"][0])
            elif selected_brand == "2":
                print("Here is the most recommended car for you:")
                print(supercars["2"]["luxury"]["Rolls-Royce"][1])
            elif selected_brand == "3":
                print("Here is the most recommended car for you:")
                print(supercars["2"]["luxury"]["Rolls-Royce"][2])
            else:
                print("Invalid selection.")
        elif category == "sports":
            print("Here are some sports cars within your budget:")
            print(supercars["2"]["sports"]["Mercedes-AMG"])
            print("\n")
            print(supercars["2"]["sports"]["Lamborghini"])
            print("\n")
            print(supercars["2"]["sports"]["Ford"])
            print("\n")
            selected_brand = input("Which brand would you like (Type the brand name)? ").strip().lower()
            print("Here is the most recommended car for you:")
            if selected_brand == "mercedes-amg":
                print("Your recommended car is:")
                print(supercars["2"]["sports"]["Mercedes-AMG"])
            elif selected_brand == "lamborghini":
                print("Your recommended car is:")
                print(supercars["2"]["sports"]["Lamborghini"])
            elif selected_brand == "ford":
                print("Your recommended car is:")
                print(supercars["2"]["sports"]["Ford"])
            else:
                print("Invalid brand selection.")
    elif budget == "3":
        category = input("Do you prefer 'luxury' or 'sports' cars? ").strip().lower()
        if category not in supercars[budget]:
            print("Invalid category. Please choose 'luxury' or 'sports'. Please run again.")
        elif category == "luxury":
            print("Here are some luxury cars within your budget:")
            print(supercars["3"]["luxury"]["Bugatti"][0])
            print("\n")
            print(supercars["3"]["luxury"]["Bugatti"][1])
            print("\n")
            selected_brand = input("Which model would you like(Type 1 for the first option, 2 for the second option? ").strip().lower()
            print("Here is the most recommended car for you:")
            if selected_brand == "1":
                print("Your recommended car is:")
                print(supercars["3"]["luxury"]["Bugatti"][0])
            elif selected_brand == "2":
                print("Your recommended car is:")
                print(supercars["3"]["luxury"]["Bugatti"][1])
            else:
                print("Invalid selection.")
        elif category == "sports":
            print("Here are some sports cars within your budget:")
            print(supercars["3"]["sports"]["Porsche"])
            print("\n")
            print(supercars["3"]["sports"]["McLaren"])
            print("\n")
            print(supercars["3"]["sports"]["Ferrari"])
            print("\n")
            print(supercars["3"]["sports"]["Koenigsegg"])
            print("\n")
            print(supercars["3"]["sports"]["Bugatti"])
            print("\n")
            selected_brand = input("Which brand would you like (Type the brand name)? ").strip().lower()
            print("Here is the most recommended car for you:")
            if selected_brand == "porsche":
                print("Your recommended car is:")
                print(supercars["3"]["sports"]["Porsche"])
            elif selected_brand == "mclaren":
                print("Your recommended car is:")
                print(supercars["3"]["sports"]["McLaren"])
            elif selected_brand == "ferrari":
                print("Your recommended car is:")
                print(supercars["3"]["sports"]["Ferrari"])
            elif selected_brand == "koenigsegg":
                print("Your recommended car is:")
                print(supercars["3"]["sports"]["Koenigsegg"])
            elif selected_brand == "bugatti":
                print("Your recommended car is:")
                print(supercars["3"]["sports"]["Bugatti"])
            else:
                print("Invalid brand selection.")
    else:
        print("Invalid budget range. Please choose from 'under 250k', '250k to 1m', or 'over 1m'. Please run again.")

car_adviser()
print("Thank you for using the Supercar Adviser!")
print("If you want to learn more, please go to the Supercar Adviser Website(it is the project called SupercarAdviserWebsite).")