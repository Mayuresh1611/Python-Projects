from os import stat
from turtle import Turtle , Screen
from time import sleep
import pandas

class StateLocater(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.data = pandas.read_csv('stateList.csv')
        self.states_list = self.data['state'].to_list()
        self.goto(-119 ,186)
    
    def locate_state(self, state_name):
        if self.states_list.count(state_name) != 0:
            state_info = self.data[self.data['state'] == state_name]    
            x = int(state_info['X_cor'])
            y = int(state_info['Y_cor'])

            self.goto(x , y)
            self.write(state_name.upper() , True , 'center' , ('Berlin Sans FB Demi' , 13 , 'normal'))
            sleep(0.5)
            return True


        else :
            self.goto(0,280)
            self.write("Wrong Input", True , 'center' , ('Berlin Sans FB Demi' , 13 , 'normal'))
            sleep(2)
            return False

    def end(self):
        self.clear()
        self.goto(94,191)
        self.write('YOU ARE GOOD' , False , 'center' , ('impact' , 10 , 'normal'))
        



