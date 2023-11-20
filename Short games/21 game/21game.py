# to get random cards
from random import  randint
# to clear the output terminal
import os

def computer (cards:list):
    # this function helps computer pick desired cards to  win
    # this function sums cards but also add them to list at same time to 
    # later see on terminal
    
    while score_adder(cards) <= 14:
        y = randint(1,13)
        cards.append(y)
        
    return score_adder(cards) , cards
    


def score_adder(cards:list):
    # this function adds up the cards gained by player
    score = 0
    for i in range(0,len(cards)):
        score += cards[i]
    return score
    
def card_generator():
    # this is main function where cards will be gernerated and to run the game
    # thi clears the terminal for clean and neat view
    clear = lambda: os. system('cls')
    clear()

    #empty lists are created for each player
    player_cards = []
    computer_cards = []
    
    #this for loop appends initial cards to player's deck
    for i in range(0,2):
        player_cards.append(randint(1,13))
        computer_cards.append(randint(1,13))
    
    # these cards will be seen at start of the round
    print ("Your random cards are: ",player_cards)
    print ("Computer's 1st card is: ",computer_cards[0])

    #this while loop will help player to choose card
    While = True
    while While:
        ans = input("Do you want card then enter 'y' or to pass enter 'n'\n>>> ")
        if ans == 'y':
            player_cards.append(randint(1,13)) 
            print (player_cards)
        elif ans == 'n':
            print ('Ok')
            While = False
        else:
            print ("You entered wrong key")
    
    #score of player will summed up by score_adder function
    player_score = score_adder(player_cards)
    
    #this will provide the score and deck of computer which will be gererated by
    # computer itself(but it is design to get as close to 21 as possible)
    computer_score , com_cards = computer(computer_cards)

    #this prints out the score and final deck
    print ("Your score: ",player_score )
    print ("computer cards :",com_cards)
    print (" computer score ",computer_score)
    
    # from here the victory or defeat will be judged
    if player_score == 21 and computer_score == 21 :
        print ('Tie ! \nDo you want to repeat the game')
        ans = input ('\'yes\' or \'no\'')
        if ans.lower() == "yes":
            card_generator() 
        else:
            print ("Have a nice day !")
    if player_score == 21:
        print ("You have won")
    elif computer_score == 21:
        print ("You have lost")
    elif player_score > 21 :
        if player_score > computer_score:
            print ("You have lost")
    elif computer_score > 21 :
        if player_score < computer_score:
            print ("You have won")    
    elif player_score > computer_score:
        print ("You have won !")
    elif computer_score > player_score:
        print ("You have lost !")
    
    # this will ask to play again or not!
    print ("Do you want to play again ?")
    ans = input ('\'yes\' or \'no\'')
    if ans.lower() == "yes":
        card_generator() 
    else:
        print ("Have a nice day !")
    
# this simply starts the whole game 
card_generator()

