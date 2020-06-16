import random
chosen = random.choice(['python', 'java', 'kotlin', 'javascript'])
print('H A N G M A N\n')
hidden = list('-' * len(chosen))
guesses = 8
letter_used = []
while guesses > 0:
    print()
    print(''.join(hidden))
    guess = input('Input a letter: ')

    if guess in chosen:
        for i in range(len(chosen)):
            if chosen[i] == guess:
                hidden[i] = guess
                
        if guess in letter_used:
            print("No improvements!")
            guesses -= 1
    else:
        print('No such letter in the word\n')
        guesses -= 1
    
    if '-' not in hidden:
        print(chosen)
        print("You guessed the word!")
        print("You survived!")
        guesses = -1
    elif guesses == 0 and '-' in hidden:
        
        print("You are hanged!")
    letter_used.append(guess)
