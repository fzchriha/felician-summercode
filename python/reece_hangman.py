import random
# Write your code here
languages = ['python', 'java', 'kotlin', 'javascript']
choose = random.choice(languages)

def get_word():
  word = random.choice(languages)
  return word

def hangman():
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 8
 

while not guessed and tried > 0:
  user = input ("Input a letter: ")
  if len(guess) == 1 and gues.isalpha():

  elif len(guess) == len(word) and guess.isalpha():
  
  else:
    print("No such letter in the word")
