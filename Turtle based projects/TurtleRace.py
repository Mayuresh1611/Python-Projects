from turtle import _Screen, Screen, Turtle, textinput
from random import randint 

screen = Screen()
screen.setup(width=800 , height=400)

race = False
user_bait = textinput("Select your bait !!" , "Which color of turtle you will bait ?")
color = ['red','orange','yellow','green','blue','purple']
turtles = []
y = -140
for i in color:
    popy = Turtle("turtle")
    popy.color(i)
    popy.penup()
    y += 40
    popy.goto(-360,y)
    turtles.append(popy)
print (turtles)
    
if user_bait:
    race = True
while race:
    
    for i in turtles:
        if i.xcor() > 370:
            race = False    
            winner_turtle = i.pencolor()
            if user_bait == winner_turtle: 
                print ("You Won !!!")
            else:
                print ("You lost !!!")
                
        x = randint(10,30)
        i.forward(x)
    

screen.exitonclick()