#to get random choice from given data
from random import choice, choices, random 
#Data for instagram follwers
from DATA import data
#for clearing purpose
import os

# this will run the game 
def play():
    clear = lambda: os. system('cls')
    clear()
    print ("""In this game there will be two instgram personalities given
    You have to choose which personality have highest no. of followers
    if you get it right your score will increase by 1 if not the game will be terminated.
    Let's Begin""")
    Engine()


#"rand_person()"The function will generate random persons
def rand_person():
    person = choice(data)
    return person

#info()This function will print out info and option of that person
def info(person1 , person2):
    if person1 == person2:
        person2 = rand_person()
    print (" A ---> %s , %s , %s"% (person1['name'],person1['description'],person1['country']))
    print (" B ---> %s , %s , %s"% (person2['name'],person2['description'],person2['country']))
    print(person1['follower_count'])
    print(person2['follower_count'])

#This will compare ans
def compare(person1,person2,ans):
    if person1['follower_count'] > person2['follower_count']:
        return ans == 'a'
    
    if person1['follower_count'] < person2['follower_count']:
        return ans == 'b'
 


#This function will run the game
def Engine():
    #"rand_person()"The function will generate random persons
    person1 = rand_person()
    person2 = rand_person()
    
    #This will run until user guesses right answer
    guess = True
    score = 0
    while guess:
        
        print("Score : ",score)
        #info()This function will print out info and option of that person
        info(person1,person2)
        
        ans = input (" A or B").lower()
        #This will compare the answer
        answer  = compare(person1,person2,ans)
        if answer == True:
            
            score += 1
            person1 = person2
        elif answer == False:
            print("Wrong!")
            print ("This is your final score: ",score)
            guess = False

            play_again = input ("Would you like to play again?\n y or n").lower()
            if play_again == 'y':
                play()
            elif play_again =='n':
                print ("Have a nice Day !!")
        else:
            print ("Wrong input game terminated")
            guess = False
        print("Right")
        clear = lambda: os. system('cls')
        clear()
        person2 = rand_person()
    print ("Game Terminated")

play()

