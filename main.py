import sys


class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550

    def const_texts(self):
        print("The coffee machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.coffee, " of coffee beans")
        print(self.cups, " of disposable cups")
        print(self.money, " of money")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        new_water = int(input())
        self.water += new_water

        print("Write how many ml of milk do you want to add:")
        new_milk = int(input())
        self.milk += new_milk

        print("Write how many grams of coffee beans do you want to add:")
        new_coffee = int(input())
        self.coffee += new_coffee

        print("Write how many disposable cups of coffee do you want to add:")
        new_cups = int(input())
        self.cups += new_cups

        # const_texts()

    def take(self):
        print("I gave you $", self.money)
        self.money = 0
        print()
        # const_texts()

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        option = input()
        if option == "1":

            if self.water - 250 < 0:
                print("Sorry, not enough water!")
            elif self.coffee - 16 < 0:
                print("Sorry, not enough coffee!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
        elif option == "2":

            if self.water - 350 < 0:
                print("Sorry, not enough water!")
            elif self.coffee - 20 < 0:
                print("Sorry, not enough coffee!")
            elif self.milk - 75 < 0:
                print("Sorry, not enough milk!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.cups -= 1
                print("I have enough resources, making you a coffee!")

        elif option == "3":

            if self.water - 200 < 0:
                print("Sorry, not enough water!")
            elif self.coffee - 12 < 0:
                print("Sorry, not enough coffee!")
            elif self.milk - 100 < 0:
                print("Sorry, not enough milk!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough cups!")
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.cups -= 1
                print("I have enough resources, making you a coffee!")

        elif option == 'back':
            self.intro()
        else:
            print("Invalid option")
        # const_texts()

    def intro(self):
        while True:
            # const_texts()
            print()
            print("Write action (buy, fill, take, remaining, exit):")
            choice = input()

            if choice == 'buy':
                self.buy()
            elif choice == 'fill':
                self.fill()
            elif choice == 'take':
                self.take()
            elif choice == 'remaining':
                self.const_texts()
            elif choice == 'exit':
                sys.exit()
            else:
                print("Invalid choice. Try again")
                self.intro()


cm = CoffeeMachine()
cm.intro()
