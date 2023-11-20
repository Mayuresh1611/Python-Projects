from turtle import Turtle 

class Devider():
    def __init__(self):
        """creates the devider between two players on the screen"""
        gap = 280
        for i in range(15):
            devider = Turtle()
            devider.shape('square')
            devider.penup()
            devider.shapesize(stretch_len= 0.3 , stretch_wid= 0.8)
            devider.color('white')
            devider.goto(0,gap)
            gap -= 40

class Score(Turtle):

    def __init__(self,x_cor , y_cor):
        '''creates the score board for each player on desired position'''
        super().__init__()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
    
        self.goto(x_cor , y_cor)
        self.write(f"{self.score}",False, 'center',('Impact',60, 'normal'))
        
    def score_inc(self):
        '''increases the displayed score by 1 '''
        self.clear()
        self.score += 1
        self.write(f"{self.score}",False, 'center',('Impact',60, 'normal'))