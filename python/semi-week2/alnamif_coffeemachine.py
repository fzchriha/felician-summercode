class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.dis_cups = 9
        self.money = 550

    def state(self):
        print(f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee} of coffee beans
        {self.dis_cups} of disposable cups
        {self.money} of money"""
              )
        self.action_prepared()

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.coffee += int(input('Write how many grams of coffee beans do you want to add:'))
        self.dis_cups += int(input('Write how many disposable cups of coffee do you want to add:'))
        self.action_prepared()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        self.action_prepared()

    def action_prepared(self):
        arg = input('Write action (buy, fill, take, remaining, exit):')
        if arg == 'buy':
            self.buy()
        elif arg == 'fill':
            self.fill()
        elif arg == 'remaining':
            self.state()
        elif arg == 'exit':
            exit()
        elif arg == 'take':
            self.take()
        else:
            self.action_prepared()

    def buy(self):
        type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - return to main menu:')
        if type == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.coffee < 16:
                print('Sorry, not enough coffee beans!')
            elif self.dis_cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.dis_cups -= 1
                print('I have enough resources, making you a coffee!')
        elif type == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.coffee < 20:
                print('Sorry, not enough coffee beans!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.dis_cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                self.water -= 350
                self.coffee -= 20
                self.milk -= 75
                self.money += 7
                self.dis_cups -= 1
                print('I have enough resources, making you a coffee!')
        elif type == 'back':
            self.action_prepared()
        else:
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.coffee < 12:
                print('Sorry, not enough coffee beans!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.dis_cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                self.water -= 200
                self.coffee -= 12
                self.milk -= 100
                self.money += 6
                self.dis_cups -= 1
                print('I have enough resources, making you a coffee!')
        self.action_prepared()


machine = CoffeeMachine()
machine.action_prepared()
