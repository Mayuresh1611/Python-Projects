from turtle import Screen

class Prompt():

    def __init__(self):
        self.screen = Screen()
        self.score  = 0

    def user_input(self):
        text = self.screen.textinput(f'SCORE :{self.score}/15','Enter Name Of State')
        return text

    def score_inc(self):
        if self.score == 14:
            return False
        else:
            self.score += 1
            return True