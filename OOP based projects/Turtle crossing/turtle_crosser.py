from turtle import Turtle

class WalkingTurtle(Turtle):
    
    def __init__(self):
        super().__init__()

        '''setups the turtle'''
        self.penup()
        self.color('green')
        self.shape('turtle')
        self.shapesize(stretch_len = 1.5 , stretch_wid= 1.5)

        '''setups it's position'''
        self.setheading(90)
        self.goto(0, -270)

    def move_forward(self):
        '''Moves turtle forward by 20 paces'''
        self.forward(20)

    def reposition(self):
        '''repositions the turtle at bottom of screen'''
        self.setheading(90)
        self.goto(0, -270)
