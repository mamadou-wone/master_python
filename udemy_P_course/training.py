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

def compare(firstData={} , secondData = {}):
  if firstData == secondData:
    secondData = chooseData(data)
  else:
    print("Compare A : " + firstData['name'] + ", a "  + firstData['description'] + " , "+ " from " + firstData['country'])        
    print(vs)
    print("Against B : " + secondData['name'] + ", a "  + secondData['description'] + " , "+ " from " + secondData['country']) 


win = False


def checkAnsuwer(answer , firstData = {} , secondData = {} , data = []):
    if answer == "A" and firstData['follower_count'] > secondData['follower_count']:
        print('You win continu ! ')
        win = True
        secondData = chooseData(data)
        compare(firstData, secondData)
    elif answer == "B" and firstData['follower_count'] < secondData['follower_count']:
        thirdData = chooseData(data)
        firstData = secondData
        secondData = thirdData
        print('You Win continu ! ')
        win = True
        compare(firstData, secondData)  
    else:
      print("You Loose ")        
      win = False
    
compare(firstData , secondData)     
answer = input("Who has more followers? Type 'A' or 'B' : ")

checkAnsuwer(answer , firstData , secondData , data)    
    