menu = {
    "espresso": {
        "Ingridents": {
            "water": 200,
            "coffee": 100
        },
        "cost": 55
    },
    "Latte": {
        "Ingridents": {
            "water": 200,
            "coffee": 100,
            "milk": 400
        },
        "cost": 70
    },
    "cappuccino": {
        "Ingridents": {
            "water": 200,
            "coffee": 100,
            "milk": 400
        },
        "cost": 70
    }
}

resource = {"water": 800, "coffee": 500, "milk": 1000, "Money": 500}
profit = 0

def resource_sufficient(order_ingridents):
    for item in order_ingridents:
        if order_ingridents[item] > resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

def coin(cost_of_drink):
    five_coin = int(input("Coin of Rs 5: ")) * 5
    ten_coin = int(input("Coin/Note of Rs 10: ")) * 10
    twenty_coin = int(input("Coin/Note of Rs 20: ")) * 20
    fifty_coin = int(input("Note of Rs 50 : ")) * 50
    sum = int(five_coin + ten_coin + twenty_coin + fifty_coin)
    return sum

def make_coffee(drink_name, order_ingridents):
    for item in order_ingridents:
        resource[item] -= order_ingridents[item]
    print(f"Here is your {drink_name} ☕")

def other_calculation(money_recieved, cost_of_drink):
    global profit
    if money_recieved > cost_of_drink:
        balance_money = money_recieved - cost_of_drink
        profit = profit + cost_of_drink
        print(f"Here is Your balance Money {balance_money}")
        make_coffee(choice, drink['Ingridents'])
    elif money_recieved < cost_of_drink:
        print(f"Sorry not Enough Money. {money_recieved} Money refunded.")
    else:
        make_coffee(choice, drink['Ingridents'])
        profit = profit + cost_of_drink

is_it_over = True
while is_it_over:
    choice = input("What would you like? (espresso/Latte/cappuccino) :")
    if choice == "espresso" or choice == "Latte" or choice == "cappuccino":
        drink = menu[choice]
        available=resource_sufficient(drink['Ingridents'])
        if available:
          payment = coin(drink['cost'])
          other_calculation(payment, drink['cost'])
        else:
          is_it_over=False
    elif choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"coffee: {resource['coffee']}ml")
        print(f"Milk : {resource['milk']}ml")
        print(f"Money : Rs {profit}")
    elif choice == "off":
        is_it_over = False
