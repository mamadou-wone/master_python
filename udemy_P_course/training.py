#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

import random
#Step 1 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

randomWord = random.choice(word_list)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# print(randomWord)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print("Choosen Word is " + randomWord)
correct_word = []

 



for i in range(len(randomWord)):
    correct_word.append('_')

life = 6
wrong = False  

while correct_word != list(randomWord):

    userLetter = input("Gess a letter : ").lower()
    for i in range(len(randomWord)):
        if randomWord[i] == userLetter:
            correct_word[i] = userLetter
        elif userLetter not in list(randomWord):
            wrong = True
            
    if wrong:
        life -= 1
        print(life)
    
    print(correct_word)
    if life == 0 and '_' in randomWord:
        print("Game Over")
        break
    if correct_word == list(randomWord):
        print("You win")        

# print(correct_word) a
