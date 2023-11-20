from turtle import Turtle
from time import sleep




class Score (Turtle):

    def __init__(self):

        with open('score.txt') as ScoreFile :
            HighScore =int( ScoreFile.read())

        """Initiates the score class
         + hideturtle 
         + moves the score to up
         + write's the score on the screen """

        self.score = 0
        self.highscore = HighScore 
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"SCORE: {self.score}  HIGHSCORE : {self.highscore} ", False,'center',('Britannic Bold', 15, 'normal'))
    

    def score_adder(self):

        """this adds the score when method is called 
         + clears the previous written string(score)
         + adds the by 1
         + writes the new score"""

        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}  HIGHSCORE : {self.highscore} ",False,'center',('Britannic Bold', 15, 'normal'))
    

    def end_score(self):

        """Writes the game over message on screen with the final score
         + clears the previous written string (score)
         + changes font(turtle) color to red
         + goes to center and writes Game Over
         + goes down amd writes the final score"""

        self.clear()
        self.color('red')
        self.goto(0,0)
        self.write("GAME\nOVER",False,"center",('Bauhaus 93', 70, 'normal'))
        self.goto(0,-80)
        self.write(f" SCORE : {self.score}\nHIGHSCORE : {self.highscore}",False,'center',('Britannic Bold', 20, 'normal'))
        
        sleep(3)
        
        self.clear()
        
    def high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('score.txt' , 'w') as ScoreFile :
                ScoreFile.write(str(self.highscore))
               

open('../file.py' , 'w')
        
        
        
        
        
            
