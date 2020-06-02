
animals = [camel, lion, deer, goose, bat, rabbit]

# write your code here
while True:
    x = input("Which habitat # do you need?")
    if x!='exit':
        print(animals[int(x)])
    elif x == 'exit':
        print("See you!")
        break
