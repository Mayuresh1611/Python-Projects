from turtle import Turtle 
from random import randint
from time import sleep, time

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        """creates a circular ball with radius of 10 """

        self.shape('circle')
        self.penup()
        self.color('white')
        self.time = 0.08
        self.x = 10
        self.y = 10
        
        
    def move(self): 
        '''moves the ball in x and y coordintes  assigned to it'''
        sleep(self.time)  
        new_x = self.xcor() + self.x  
        new_y = self.ycor() + self.y 
        self.goto(new_x , new_y)

    def bounce_y (self):
        """ball changes its y coordinates to opposite diection"""
        self.y *= -1

    def bounce_x (self):
        """ball changes it's x coordinates to opposit direction
        and also increases the speed of ball"""
        self.time -=  0.005
        self.x *= -1

    def reposition(self):
        """ball repositions to origin and released in opposite direction of previous direction"""
        self.time = 0.1
        self.goto(0,0)
        sleep(1)
        self.bounce_x()