import random
import sys

def game():
    wordList = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(wordList)
    answer = list(word)
    dashes = len(answer) * '-'
    shadowList = list(len(answer) * '-')
    
    userInputsUsed = set()
    
    print("H A N G M A N")
    repeated_words = []
    
    count = 0
    while count < 8:
        print()
        print(dashes)
        if shadowList == answer:
            print("You guessed the word!")
            print("You survived!")
            break
        userInput = input("Input a letter: ")
        repeated_words.append(userInput)
        if len(userInput) > 1:
            print("You should input a single letter")
        elif userInput.islower() != True:
            print("It is not an ASCII lowercase letter")    
        elif repeated_words.count(userInput) > 1:
            print("You already typed this letter")
        elif userInput in word:
            placed = [p for p, x in enumerate(word) if x == userInput]
            for i in placed:
                shadowList[i] = userInput
            userInputsUsed.add(userInput)
            dashes = "".join(shadowList)
        elif userInput not in wordList:
            count += 1
            print("No such letter in the word")
    if shadowList != answer:
        print("You are hanged!")

play = input('Type "play" to play the game, "exit" to quit: ')

if play == "play":
    game()

elif play == "exit":
    sys.exit(0)
