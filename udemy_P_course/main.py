#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

from training import MENU, resources

# print(MENU["espresso"]['ingredients']['water'])
def showMenu(name , ingredients , value , menu = {}):
    return menu[name][ingredients][value]


def showCoffePrice(name , value , menu ={}):
    return menu[name][value]
# print(showMenu("cappuccino", "ingredients", "coffee" , MENU))
# print(type(showCoffePrice("cappuccino", "cost" , MENU)))

resources["money"] = 0
def getResource(resources = {}):
    for i in resources:
        print(i.title() + ": " + str(resources[i]))
 
def getRessourceValue(value , resources = {}):
    return resources[value]

# print(getRessourceValue("water", resources))
        
def updateResource(resources = {} , water=0 , milk =0,coffee = 0, money = 0):
    resources["water"] = water
    resources["milk"] = milk
    resources["coffee"] = coffee
    resources["money"] = money
    
    
def calculatePrice(quarter , dime , nickel , pennies):
    total = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + pennies * 0.01
    return total

# userMoney = calculatePrice( 6 , 5 , 4 , 2)

def chekPrice(total , coffeeName , menu = {}):
    cost = menu[coffeeName]["cost"]
    money = getRessourceValue("money",resources)
    # water = showMenu(coffeeName, "ingredients", "water" , MENU)
    if coffeeName == "espresso":
        milkGram = 0     
    else:
        milkGram =  showMenu(coffeeName, "ingredients", "milk" , MENU)   
        
    # coffee = showMenu(coffeeName, "ingredients", "coffe" , MENU)
    water = getRessourceValue("water", resources) - showMenu(coffeeName, "ingredients", "water" , MENU)
    milk = getRessourceValue("milk", resources) - milkGram
    coffee = getRessourceValue("coffee", resources) - showMenu(coffeeName, "ingredients", "coffee" , MENU)
    change = 0
    
    
    if total == cost:
        change = 0
        print(f"Here is ${change} in change")
        print(f"Here is your {coffeeName} ☕️. Enjoy!")
        money += cost
        updateResource(resources, water , milk , coffee , money)
    elif total > cost:
        change = total - cost
        print(f"Here is ${change} in change")
        print(f"Here is your {coffeeName} ☕️. Enjoy!")
        money += cost
        updateResource(resources, water , milk , coffee , money)
    elif total < cost:
        change = total
        print("Sorry that's not enough money. Money refunded.")
    else:
        print("Error")    
        
# print(chekPrice(100 , "cappuccino" , MENU))

def ressourceStat(coffeeName, resource = {}):
    cost = MENU[coffeeName]["cost"]
    water = MENU[coffeeName]["ingredients"]["water"]
    if coffeeName == "espresso":
        milk = 0
    else:
        milk = MENU[coffeeName]["ingredients"]["milk"]    
    coffee = MENU[coffeeName]["ingredients"]["coffee"]
    if water > resources['water'] or milk > resources['milk'] or coffee > resource['coffee']:
        print("Sorry There is enought water")
    else:
        inputMoney(coffeeName)

def inputMoney(coffeeName):        
    quarter = int(input("How many quarter? : "))
    dimes = int(input("How many dimes? : "))
    nickel = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))
    total = calculatePrice(quarter ,dimes , nickel , pennies)
    chekPrice(total , coffeeName , MENU)
    # print(total)
    
while  True:   
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        getResource(resources)
    elif choice == "espresso":
        ressourceStat("espresso" , resources)
        # getResource(resources)
    elif choice == "latte":
        ressourceStat("latte" , resources)
        # getResource(resources)      
    elif choice == "cappuccino":
        ressourceStat("cappuccino" , resources)
        # getResource(resources)
    else:
        print("Error")    
