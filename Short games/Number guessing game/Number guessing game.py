#to get random number
from random import randint
# to clear the output terminal
import os

#this function will generate random number 
def rand_no ():
    num = randint(1,100)
    return num

#this fuction will handle guessing
def guess (num:int , attempt:int):
    print ("Please select number between 1 to 100")
    guess = False
    
    while not guess:
        print ("Remaining attempts : ",attempt)
        
        guess_num = int(input("please enter no.\n>>> "))
        if guess_num == num:
            print("correct guess !")
            guess = True
            play_again()
            
        elif guess_num > num:
            print ("Too High !")
            attempt -= 1
        elif guess_num < num:
            attempt -= 1
            print ("Too low !")
        if attempt == 0:
            print ("correct answer was : ",num)
            print ("You are out of attempts , sorry!")
            guess = True
            play_again()
            
#this function will provide play again option
def play_again():

    ans = input("would you like to play again?\n \"Yes\" , \"no\"\n>>> ").lower()
    if ans == 'yes':
        run()
    elif ans == 'no':
        print ("Thank you for playing !")
    else :
        play_again()


# this fuction will start the game 
def run ():
    #this will collect the diffculty
    print ("Welcome to number guessing game")
    ans = input("Which difficulty level you would like to play\n\t \"high\"\t \"low\"\n>>> ").lower()
    
    #this will give out no. of attempts
    if ans == 'high':
        print ("you have 7 attempts to guess")
        attempt = 7
    elif ans == 'low':
        print ("you have 12 attempts to guess")
        attempt = 12
    else :
        print ("wrong input")
        run()
    guess (rand_no(),attempt)
    
#starts the game
run()
