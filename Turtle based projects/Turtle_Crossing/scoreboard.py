from turtle import Turtle

class Levels(Turtle):

    def __init__(self):

        '''setups the level text on top left corner of screen'''
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-230 , 260)
        self.write(f"LEVEL : {self.level}",False ,'center' , ('Roboto Black', 20, 'normal') )

    def level_inc(self):
        '''increases the level (text only)'''
        self.clear()
        self.level += 1
        self.write(f"LEVEL : {self.level}",False ,'center' , ('Roboto Black', 20, 'normal') )

    def game_over(self):
        '''displays game over text'''
        self.goto(0,250)
        self.write(f"GAME OVER !",False ,'center' , ('Roboto Black', 30, 'normal') )
        
        