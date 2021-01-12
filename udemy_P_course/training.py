#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|
import random                                 

random_int = random.randint(0 , 4)

# name = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

# print(name[random_int] + " is going to buy the meal today!")

# name_string = input("Give me the name ")

# name = name_string.split(', ')

# print(name[random_int] + " is going to buy the meal today!")

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
choice = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# choice = input("Enter your choice ")

column = int(choice[0]) - 1
row = int(choice[1]) - 1 

map[row][column] = "X"




#Write your code above this row 👆
# Ligne/column
# print(map[1][2])
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")