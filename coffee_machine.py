class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = "selecting action"

    def status(self):
        print()
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.disposable_cups) + " of disposable cups")
        print(str(self.money) + " of money")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.beans += int(input("Write how many ml of beans do you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def buy(self):
        selection = self.selection(input("What do you want to buy? 1 - espresso, "
                                         "2 - latte, 3 - cappuccino, back - to main menu \n"))

        if selection == "back":
            return
        elif selection == 1:
            espresso = CoffeeType(250, 0, 16, 4)
            if CoffeeMachine.can_make(self, espresso):
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.make_coffee(self, espresso)
        elif selection == 2:
            latte = CoffeeType(350, 75, 20, 7)
            if CoffeeMachine.can_make(self, latte):
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.make_coffee(self, latte)
        elif selection == 3:
            cappuccino = CoffeeType(200, 100, 12, 6)
            if CoffeeMachine.can_make(self, cappuccino):
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.make_coffee(self, cappuccino)

    def can_make(self, coffee: "CoffeeType"):
        if self.water - coffee.water_per_cup < 0:
            print("Sorry, not enough water!")
            return False
        elif self.beans - coffee.beans_per_cup < 0:
            print("Sorry, not enough coffee beans!")
            return False
        elif self.milk - coffee.milk_per_cup < 0:
            print("Sorry, not enough milk!")
            return False
        elif self.disposable_cups - 1 < 0:
            print("Sorry,not enough disposable cups!")
            return False
        else:
            return True

    def make_coffee(self, coffee: "CoffeeType"):
        self.water -= coffee.water_per_cup
        self.milk -= coffee.milk_per_cup
        self.beans -= coffee.beans_per_cup
        self.money += coffee.cost
        self.disposable_cups -= 1

    def selection(self, action):
        if self.state == "selecting action":
            if action == "buy":
                self.state = "choosing a type of coffee"
                CoffeeMachine.buy(self)
            elif action == "fill":
                CoffeeMachine.fill(self)
            elif action == "take":
                CoffeeMachine.take(self)
            elif action == "remaining":
                CoffeeMachine.status(self)
            elif action == "exit":
                return -1

        elif self.state == "choosing a type of coffee":
            if action == "back":
                self.state = "selecting action"
                return "back"
            elif action == "1":
                self.state = "selecting action"
                return 1
            elif action == "2":
                self.state = "selecting action"
                return 2
            elif action == "3":
                self.state = "selecting action"
                return 3


    def run(self):
        while True:
            print()
            selection = self.selection(input("Write action (buy, fill, take, remaining, exit) \n"))
            if selection == -1:
                break


class CoffeeType:

    def __init__(self, water_per_cup, milk_per_cup, beans_per_cup, cost):
        self.water_per_cup = water_per_cup
        self.milk_per_cup = milk_per_cup
        self.beans_per_cup = beans_per_cup
        self.cost = cost


coffee_machine = CoffeeMachine()
coffee_machine.run()

