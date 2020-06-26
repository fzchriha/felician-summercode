import random
name = input("Enter your name: ")
print("Hello,"+name)
score = 0
rating = 'rating.txt'
file = open('rating.txt', 'a')
file.write(name+': ')
file.close()
options = "rock,paper,scissors".split(',')
modified_options = input()
if len(modified_options) > 0:
    options = modified_options.split(',')
    print("Okay, let's start")

print("*******GAME START********")
while True:

    computer = options[random.randint(0, len(options) - 1)]
    user = input()

    if user == "!exit":
        print("Bye!")
        break

    if user == "!rating":
        print("Your rating: {}".format(score))
        continue

    if user not in options:
        print("Invalid input")
        continue

    comp_idx = options.index(computer)
    user_idx = options.index(user)
    if user_idx > comp_idx:
        user_idx -= len(options)

    if user == computer:
        print("There is a draw (" + computer + ")")
        score += 50
    elif comp_idx - user_idx <= len(options) // 2:
        print("Sorry, but computer chose " + computer)
    else:
        print("Well done. Computer chose " + computer + " and failed")
        score += 100
        
file = open('rating.txt', 'a')
file.write(''+str(score)+'\n')
file.close()
