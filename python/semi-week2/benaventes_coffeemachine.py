#hey fatima! I'm still editing this. I just learned I can resubmit on jetbrains lol. 

import sys #import sys module for exit

water, milk, beans, cups, money = 400, 540, 120, 9, 550

def remain(x):#simply tells you what remains in the machine
    print()
    print("The coffee machine has: ")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print("$", money, "of money")
    print()


def check(water_, milk_, beans_, cups_): #checks if there's enough resources
    global water, milk, beans, cups, money #global makes it be able to get the values from the water, milk, beans, cups, money outside the function
    no = "Sorry, not enough"
    status = False
    
    #if the value available is less than or equal to the values asked for
    if water <= water_:
        print(no, "water!")
        print()
        main()
    elif milk <= milk_:
        print(no, "milk!")
        print()
        main()
    elif beans <= beans_:
        print(no, "coffee beans!")
        print()
        main()
    elif cups <= cups_:
        print(no, "disposable cups!")
        print()
        main()
    else:
        status = True
    return status
        


def buy(x): #where user can make a choice
    print()
    global water, milk, beans, cups, money

    choose = input("What do you want to buy? 1 -espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    yes = "I have  enough resources, making you a coffee!"
    
    #if statements based on user input decisions. 
    #reduces based on amounts, increases money gained.
    if choose == "1":
        if check(250, 0, 16, 1):
            water -= 250
            milk -= 0
            beans -= 16
            cups -= 1
            money += 4
            print(yes)
 
    elif choose == "2":
        if check(350, 75, 20, 1):
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7  
            print(yes)

    elif choose == "3":
        if check(200, 100, 12, 1):
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6 
            print(yes)

    elif choose == "back":
        main()

    else:
        print("Wrong action")
        buy()
    print()

        
def fill(x): #asks user how much more they want to add to the machine and it += to values above
    global water, milk, beans, cups, money
    
    #asks for input on what to add, and whatever is inputed increases the value corresponding to it
    water += int(input("Write how many ml of water do you want to add:\n"))

    milk += int(input("Write how many ml of milk do you want to add:\n"))

    beans += int(input("Write how many grams of coffee beans do you want to add:\n"))

    cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    print()


def take(x): #outputs money given based on price of drinks
    global money
    
    print("I gave you $", money)
    print()
    money = 0
   

def main(): #main function of coffee machine that performs all above methods/functions
    loop = True
    
    #while loop for looping through user input until user chooses "exit"
    while loop:
        action = input("Write action (buy, fill, take, remaining, exit): ")
        
        #calls on function based on what user inputted for value "action"
        if action == "buy":
            buy(action)

        elif action =="fill":
            fill(action)

        elif action == "take":
            take(action)

        elif action == "remaining":
            remain(action)

        elif action == "exit":
            sys.exit(1) #used to end the program
            
main() #call main function to run entire program
