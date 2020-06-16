water = 400
milk = 540
coffee = 120
cups = 9
money = 550


def const_texts():
    print("The coffee machine has:")
    print(water, " of water")
    print(milk, " of milk")
    print(coffee, " of coffee beans")
    print(cups, " of disposable cups")
    print(money, " of money")


def fill():
    global water
    global milk
    global coffee
    global cups
    print("Write how many ml of water do you want to add:")
    new_water = int(input())
    water += new_water

    print("Write how many ml of milk do you want to add:")
    new_milk = int(input())
    milk += new_milk

    print("Write how many grams of coffee beans do you want to add:")
    new_coffee = int(input())
    coffee += new_coffee

    print("Write how many disposable cups of coffee do you want to add:")
    new_cups = int(input())
    cups += new_cups

    const_texts()


def take():
    global money
    print("I gave you $", money)
    money = 0
    print()
    const_texts()


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    option = int(input())
    global water
    global milk
    global coffee
    global money
    global cups
    if option == 1:
        water -= 250
        coffee -= 16
        money += 4
        cups -= 1
    elif option == 2:
        water -= 350
        milk -= 75
        coffee -= 20
        money += 7
        cups -= 1
    elif option == 3:
        water -= 200
        milk -= 100
        coffee -= 12
        money += 6
        cups -= 1
    else:
        print("Invalid option")
    const_texts()


def intro():
    const_texts()
    print()
    print("Write action (buy, fill, take):")
    choice = input()

    if choice == 'buy':
        buy()
    elif choice == 'fill':
        fill()
    elif choice == 'take':
        take()


intro()
