#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

from art_hagman import  guess
from art_hagman import vs
from data import data
import random

print(guess)


# firstData = random.choice(data)
# secondData = random.choice(data)

def chooseData(data = []):
  randomData = random.choice(data)
  return randomData
    
  
firstData = chooseData(data)
secondData = chooseData(data)


def compare(firstData = {} , secondData = {},data = []):
    if firstData == secondData:
        secondData = chooseData(data)         
    else:
          print(f"Compare A: {firstData['name']} , a {firstData['description']}, from {firstData['country']} ")
          print(vs)
          print(f"Compare B: {secondData['name']} , a {secondData['description']}, from {secondData['country']} ")



win = False
score = 0
compare(firstData , secondData , data) 
while win != True: 
  answer = input("Who has more followers ? Type A or B: ")
  if answer == "A" and firstData['follower_count'] > secondData['follower_count']:
        print("You Win")
        secondData = chooseData(data)
        win = True
        score += 1
        compare(firstData, secondData, data)
        win = False
  elif answer == "B" and firstData['follower_count'] < secondData['follower_count']:
        firstData = secondData
        secondData = chooseData(data)
        win = True
        score += 1
        compare(firstData, secondData, data)
        print("You Win")
        win = False
  else:
      print('You Loose')
      win = False
      break 
              

print(f"Your score is {score}")      


# print(firstData )
# print(secondData)