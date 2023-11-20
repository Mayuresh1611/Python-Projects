from turtle import  Screen
from prompt_manager import Prompt
from state_locater import StateLocater
import pandas

screen = Screen()
screen.setup(width = 500 , height =  600)
screen.bgpic('empty_map.gif')
screen.listen()

state_locater = StateLocater()
prompt = Prompt()
game_is_on = True


while game_is_on:
    
    state  = prompt.user_input()
    ans = state_locater.locate_state(state)

    if ans:
        game_is_on = prompt.score_inc()

state_locater.end()

screen.mainloop()