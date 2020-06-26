import random
def game():
  chosen = random.choice(['python', 'java', 'kotlin', 'javascript'])
  print('H A N G M A N\n')
  hidden = list('-' * len(chosen))
  guesses = 8
  letter_used = []
  while guesses > 0:
      print()
      print(''.join(hidden))
      guess = input('Input a letter: ')
      if len(guess) == 0 or len(guess) > 1:
        print('You should enter a single letter.')
      if guess in chosen:
          for i in range(len(chosen)):
              if chosen[i] == guess:
                  hidden[i] = guess             
          if guess in letter_used and guess in chosen :
              print("You already typed this letter\n")

      elif guess.isalpha() == False or guess.islower() == False:
          print('It is not an ASCII or not a lowercase letter')
      else:
          print('No such letter in the word\n')
          guesses -= 1
      
      if '-' not in hidden:
          print()
          print(chosen)
          print("You guessed the word!\n")
          print("You survived!\n")
          guesses = -1
      elif guesses == 0 and '-' in hidden:
          
          print("You are hanged!\n")

      letter_used.append(guess)
  


game()
while True:
  print("~ ~ ~ ~ LET'S PLAY AGAIN! ~ ~ ~ ~")
  again = input("Do you want to play again? (y/n) :  ")
  if again == 'y':
    print()
    print("~ ~ ~ ~ NEW GAME ~ ~ ~ ~")
    game()
  else:
    print()
    print("Thank you for playing")
    break
