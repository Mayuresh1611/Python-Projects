from turtle import  Screen
import pandas

screen = Screen()
screen.setup(500 , 600)
screen.bgpic('empty_map.gif')


states_coord = {
    'name' : [],
    'X_cor':[],
    'Y_cor':[]
}

def position_of_click(x , y):
    name = screen.textinput(f'x: {round(x)} , y: {round(y)}' , 'Please Enter State Name ')
    states_coord['name'].append(name)
    states_coord['X_cor'].append(x)
    states_coord['Y_cor'].append(y)

    
screen.listen()
screen.onscreenclick(position_of_click)

print (states_coord)

screen.mainloop()



