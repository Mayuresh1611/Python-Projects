from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_cor,y_cor):
        super().__init__()
        """Creates the paddle of length= 60 width= 20"""
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1 , stretch_wid= 5)
        self.x = x_cor
        self.y = y_cor
        self.goto(self.x,0)


    
    def up(self):
        """Moves the paddle upwards by 50 """
        y_cor = self.ycor() + 50
        self.setpos(self.x , y_cor )
    
    def down(self):
        """Moves the paddle downwards by 50 """
        y_cor = self.ycor() - 50
        self.setpos(self.x , y_cor )
