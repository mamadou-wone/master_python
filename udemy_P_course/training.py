#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

allOption = [rock,paper,scissors]
randomChoce =  random.randint(0 , 2)


choice = input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
userChoice = allOption[int(choice)]
cumperterChoice = allOption[randomChoce]

print(userChoice)
print("Computer Choice:\n" + cumperterChoice)


if userChoice == rock and cumperterChoice == scissors:
    print("You loose")
elif userChoice == scissors and cumperterChoice == rock:
    print("You Win")
elif userChoice == scissors and cumperterChoice == paper:
    print("You Win")
elif userChoice == paper and cumperterChoice == scissors:
    print("You Loose")    
elif userChoice == paper and cumperterChoice == rock:
    print("You Win")
elif userChoice == rock and cumperterChoice == paper:
    print("You Loose")    
else:
    print("Equal")    