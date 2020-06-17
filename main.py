import sys

# The global variables
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

    # const_texts()


def take():
    global money
    print("I gave you $", money)
    money = 0
    print()
    # const_texts()


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    option = input()
    global water
    global milk
    global coffee
    global money
    global cups
    if option == "1":

        if water - 250 < 0:
            print("Sorry, not enough water!")
        elif coffee - 16 < 0:
            print("Sorry, not enough coffee!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            water -= 250
            coffee -= 16
            money += 4
            cups -= 1
            print("I have enough resources, making you a coffee!")
    elif option == "2":

        if water - 350 < 0:
            print("Sorry, not enough water!")
        elif coffee - 20 < 0:
            print("Sorry, not enough coffee!")
        elif milk - 75 < 0:
            print("Sorry, not enough milk!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            water -= 350
            milk -= 75
            coffee -= 20
            money += 7
            cups -= 1
            print("I have enough resources, making you a coffee!")

    elif option == "3":

        if water - 200 < 0:
            print("Sorry, not enough water!")
        elif coffee - 12 < 0:
            print("Sorry, not enough coffee!")
        elif milk - 100 < 0:
            print("Sorry, not enough milk!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            water -= 200
            milk -= 100
            coffee -= 12
            money += 6
            cups -= 1
            print("I have enough resources, making you a coffee!")

    elif option == 'back':
        intro()
    else:
        print("Invalid option")
    # const_texts()


def intro():
    while True:
        # const_texts()
        print()
        print("Write action (buy, fill, take, remaining, exit):")
        choice = input()

        if choice == 'buy':
            buy()
        elif choice == 'fill':
            fill()
        elif choice == 'take':
            take()
        elif choice == 'remaining':
            const_texts()
        elif choice == 'exit':
            sys.exit()
        else:
            print("Invalid choice. Try again")
            intro()


intro()
