#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|


from art_hagman import blackjack
import random
play = input("Do you want  to play tipe 'y' or 'n' ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def calculate_score(score = []):
    somme = sum(score)
    if 11 in score and 10 in score and somme == 21:
        blackjack = True
    elif 11 in score and somme > 21:
        score[score.index(11)] = 1
        somme = sum(score)
    return somme

# def compage(user_score , computer_score):
#     if condition:
        

if play == 'y':
    print(blackjack)
    for i in range(2):
        random_computer = random.choice(cards)
        random_user = random.choice(cards)
        user_cards.append(random_user)
        computer_cards.append(random_computer)

    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards} , current score : {user_score} \n Computer's first card: {computer_cards}")
    if user_score == 21 and computer_score != 21:
        print('You win')
    elif user_score != 21 and computer_score == 21:
        print('You loose')
    elif user_score == 21  and  computer_score == 21:
        print('You loosee')
                
    continu = input("Type 'y' to get another card, type 'n' to pass: ")
    while continu != 'n':
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards} , current score : {user_score} \n Computer's first card: {computer_cards}")
        user_score = calculate_score(user_cards)
        if user_score > 21:
            print('You loose')
            break
        computer_score = calculate_score(computer_cards)
        continu = input("Type 'y' to get another card, type 'n' to pass: ")
    # print(user_score)
    # print(computer_score)
else:
    exit    



#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().





  
    



# print(sum(user_cards))
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
