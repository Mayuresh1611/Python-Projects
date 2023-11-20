from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        """initiates the food class and sets food as circle with cyan color
        food goes to random location"""
        super().__init__()  
          
        self.shape("circle")   
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.penup()
        self.color('cyan')
        self.speed(0)
        rand_x = randint(-280 , 280)
        rand_y = randint(-280 , 280)

        self.goto(rand_x,rand_y)
    
    def eaten(self):
        """when the method is initiated and 
        food goes to new random position"""
        rand_x = randint(-280 , 280)
        rand_y = randint(-280 , 280)

        self.goto(rand_x,rand_y)
       