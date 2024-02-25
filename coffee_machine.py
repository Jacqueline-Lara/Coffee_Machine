MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18

        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

flag = True
money = 0
profit = 0
enough_resources = False

#Function for checking if there are enough resoures to make the beverage.
def check_resources(choice):
    check_enough_resources = []
    for beverage in MENU:
        if beverage == choice:
            menu_beverage = MENU[beverage]

            for material in menu_beverage["ingredients"]:
                menu_beverage_2 = menu_beverage["ingredients"]
                if menu_beverage_2[material]<= resources[material]:
                    check_enough_resources.append(True)
                else:
                    check_enough_resources.append(False)
                    
            if check_enough_resources[0] == True and check_enough_resources[1] == True and check_enough_resources[2] == True:
                enough_resources = True
                check_enough_resources = []
                return enough_resources
            else:
                for i in range(3):
                    elements = ["water", "milk", "coffee"]
                    if check_enough_resources[i] == False:
                        print(f"Sorry, there is not enough {elements[i]} ") 
                enough_resources = False
                check_enough_resources = []
                return enough_resources

#Function for requessting money to the user, money must be a positive digit.
def enough_money(coin):
    flag_2 = True
    while flag_2 == True: 
        money = input(f"How many {coin} will you insert ")
        if money.isdigit():
            money = int(money)
            if money < 0:
                print("Numbers cannot be negative ")
            else:
                
                flag_2 = False
                return money
        else:
            print("This is not correct, try again ")

def get_total_money():
    quarters = enough_money("quarters")
    dimes = enough_money("dimes")
    nickles = enough_money("nickles")
    pennies = enough_money("pennies")
    total_money = (quarters * 0.25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
    return total_money

def access_price(choice):
    for beverage in MENU:
        if beverage == choice:
            menu_beverage = MENU[beverage]
            return (menu_beverage["cost"])

def deduct_resources(choice):
    for beverage in MENU:
        if beverage == choice:
            menu_beverage = MENU[beverage]

            for material in menu_beverage["ingredients"]:
                menu_beverage_2 = menu_beverage["ingredients"]
                new_resource = resources[material] - menu_beverage_2[material]
                resources[material] = new_resource

    
while flag == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    choice = choice.lower()
    
    if choice == "espresso":
        enough_resources = check_resources(choice)
        
        if enough_resources == True:
            coffe_price = access_price(choice)
            print(f"This is the price of your {choice}: {coffe_price}")
            money = get_total_money()
            if money == coffe_price:
                
                print(f"Enjoy your {choice} ")
                deduct_resources(choice)
                profit = profit + coffe_price
                money = 0
            elif money > coffe_price:
                change = money - coffe_price
                
                print(f"Here is your change {change}")
                print(f"Enjoy your {choice} ")
                deduct_resources(choice)
                profit = profit + coffe_price
                money = 0
            elif money < coffe_price:
                print(f"Not enough money for your coffe, here is your money back {money}")  
                
         
    # water = 200, milk = 150, coffee = 24, money = 2.5
    elif choice == "latte":
        enough_resources = check_resources(choice)
        
        if enough_resources == True:
            coffe_price = access_price(choice)
            print(f"This is the price of your {choice}: {coffe_price}")
            money = get_total_money()
            if money == coffe_price:
                print(f"Enjoy your {choice} ")
                deduct_resources(choice)
                profit = profit + coffe_price
                money = 0
            elif money > coffe_price:
                change = money - coffe_price
                print(f"Here is your change {change}")
                print(f"Enjoy your {choice} ")
                deduct_resources(choice)
                profit = profit + coffe_price
                money = 0
            elif money < coffe_price:
                print(f"Not enough money for your coffe, here is your money back {money}")  
                money = 0  
                 
    elif choice == "cappuccino":
        enough_resources = check_resources(choice)
        
        if enough_resources == True:
            coffe_price = access_price(choice)
            print(f"This is the price of your {choice}: {coffe_price}")
            money = get_total_money()
            if money == coffe_price:
                print(f"Enjoy your {choice} ")
                deduct_resources(choice)
                profit = profit + coffe_price
                money = 0
            elif money > coffe_price:
                change = money - coffe_price
                print(f"Here is your change {change}")
                print(f"Enjoy your {choice} ")
                deduct_resources(choice)
                profit = profit + coffe_price
                money = 0
            elif money < coffe_price:
                print(f"Not enough money for your coffe, here is your money back {money}")  
                money = 0

    elif choice == "off":
        print("I will turn off in order to give you a better service ")
        flag = False
    
    elif choice == "report":
        for value in resources:
            print(f"{value} --- {resources[value]}")
        print(f"money     --- {profit}")
    else:

        print("That is not a valid option, try again please. ")










