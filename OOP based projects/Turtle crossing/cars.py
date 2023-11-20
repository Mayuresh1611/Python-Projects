from turtle import Turtle 
from random import choice, randint

# list of colors 
colors =  [ "red", "blue", "green", "yellow", "purple", "orange", 'cyan' ]

class Cars(Turtle):
    cars = []

    def __init__(self):
        super().__init__()
        '''Creates a randomly colored car '''

        self.color(choice(colors))
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid= 1 , stretch_len= 2.0)

        '''spwans car at random y position'''
        self.x = 300
        self.y = randint(-200 , 240)
        self.goto(300, self.y)
        self.speed = 10
    
        '''append created car(object) to cars list for future '''
        self.cars.append(self)

    def move(self):    

        '''moves the car forward with given speed to it ''' 
        self.x -= self.speed
        self.goto(self.x , self.y)

    def speed_inc(self , speed):
        '''increases the speed of car by taking required incrimination as input'''
        self.x -= speed