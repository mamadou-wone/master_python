#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

import random

print("Welcome to the Guessing Game !")
print("I'm thinking of a number between 11 and 100")
choose = input("Choose a difficulty . Type 'easy' or 'hard': ")

attempts = 0

if choose == "easy":
    attempts = 10
else:
    attempts = 5
        
randomNumber = random.randint(1, 100)
print(randomNumber)
def guess(randomNumber , attempts):
    print(f"You have {attempts} to guess the number")
    while attempts != 0:
        user_number = int(input("Make a guess : "))
        if user_number < randomNumber:
            print("Too Low")
        elif user_number > randomNumber:
            print("Too high")
        else:
            print(f"You guess the number {randomNumber}")
            break        
        attempts -= 1    
        print(f"You have {attempts} to guess the number")

guess(randomNumber , attempts)