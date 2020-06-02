import sys #import sys module for exit

class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        
    def main(self): #main function of coffee machine that performs all above methods/functions
        loop = True
        
        #while loop for looping through user input until user chooses "exit"
        while loop:
            action = input("Write action (buy, fill, take, remaining, exit): ")

            if action == "buy":
                self.buy()

            elif action =="fill":
                self.fill()

            elif action == "take":
                self.take()

            elif action == "remaining":
                self.remain()

            elif action == "exit":
                sys.exit(1) #used to end the program

    def remain(self):#simply tells you what remains in the machine
        print()
        print("The coffee machine has: ")
        print(water, "of water")
        print(milk, "of milk")
        print(beans, "of coffee beans")
        print(cups, "of disposable cups")
        print("$", money, "of money")
        print()


    def check(self, water_, milk_, beans_, cups_): #checks if there's enough resources
        no = "Sorry, not enough"
        status = False

        if water <= water_:
            print(no, "water!")
            print()
            self.main()
        elif milk <= milk_:
            print(no, "milk!")
            print()
            self.main()
        elif beans <= beans_:
            print(no, "coffee beans!")
            print()
            self.main()
        elif cups <= cups_:
            print(no, "disposable cups!")
            print()
            self.main()
        else:
            status = True
        return status
            


    def buy(self): #where user can make a choice
        print()
        global water, milk, beans, cups, money

        choose = input("What do you want to buy? 1 -espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

        yes = "I have  enough resources, making you a coffee!"
        
        #if statements based on user input decisions. 
        if choose == "1":
            if self.check(250, 0, 16, 1):
                water -= 250
                milk -= 0
                beans -= 16
                cups -= 1
                money += 4
                print(yes)
     
        elif choose == "2":
            if self.check(350, 75, 20, 1):
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                money += 7  
                print(yes)

        elif choose == "3":
            if self.check(200, 100, 12, 1):
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                money += 6 
                print(yes)

        elif choose == "back":
            self.main()

        else:
            print("Wrong action")
            self.buy()
        print()

            
    def fill(self): #asks user how much more they want to add to the machine and it += to values above
        global water, milk, beans, cups, money
        
        water += int(input("Write how many ml of water do you want to add:\n"))

        milk += int(input("Write how many ml of milk do you want to add:\n"))

        beans += int(input("Write how many grams of coffee beans do you want to add:\n"))

        cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        print()


    def take(self): #outputs money given based on price of drinks
        global money
        
        print("I gave you $", money)
        print()
        money = 0
       

                
    
water, milk, beans, cups, money = 400, 540, 120, 9, 550

machine = CoffeeMachine(water, milk, beans, cups, money)
machine.main()
