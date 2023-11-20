from tkinter import *
import requests
import sys
from time import sleep


URL = 'https://opentdb.com/api.php?amount=20&category=18&type=boolean'
QUESTION = 0
ANSWER = ''
SCORE = 0


'''
Class for buttons to produce buttons from image
'''

class ImageButton(Button):
    
    def __init__(self , x_cor , y_cor , image1 , image2 , *functions):

        self = Button(image= image1 , bd=0  , bg='yellow' , relief='sunken' , activebackground='yellow' )

        def pressed(_):
            self.config(image=image2) 
            for func1 in functions:
                try:
                    func1()
                except:
                    pass
              
        
        def released(_):
            self.config(image= image1)
            


        self.bind('<ButtonPress>' , pressed)
        self.bind('<ButtonRelease>' , released)

        self.place(anchor=CENTER , x=x_cor , y=y_cor)

'''
window setup
'''
window = Tk()
window.title('TRIVIA Quiz game')
window.geometry('400x550')


'''
Canvas setup
'''
canvas = Canvas(width=400,height= 550,bg='yellow')
canvas.place(anchor=CENTER , x=200 , y=275)


'''
Functions
'''
# Getting Quiz questions
response = requests.get(url=URL)
questions = response.json()
print(questions)

def score_inc():
    global SCORE
    if SCORE < 20:
        SCORE += 1
        canvas.itemconfig(score , text=f'SCORE : {SCORE}')

def fill_green():
    canvas.itemconfig(border , fill='light green')

def fill_red():
    canvas.itemconfig(border , fill='red')

def fill_white():
    canvas.itemconfig(border , fill='white')
    
def next_question():

    fill_white()
    global QUESTION , ANSWER
    
    if QUESTION < len(questions['results']):
        question = questions['results'][QUESTION]['question']
        QUESTION += 1
        canvas.itemconfig(question_text, text=question)
        ANSWER = (questions['results'][QUESTION]['correct_answer'])


    

def right():
    
    if ANSWER == 'True':
        fill_green()
        score_inc()

    else:
        fill_red()
    window.after(1300 , next_question )
    

def wrong():

    if ANSWER == 'False':
        fill_green()
        score_inc()
    else:
        fill_red()  
    window.after(1000 , next_question )
    

'''
GUI Setup 
'''
#border around question_text
border = canvas.create_rectangle( 60 , 60 , 340 , 400 , width=4 , fill='white' )

#canvas_text as question
question_text = canvas.create_text( 200 , 225 , width=240 ,  text='questionsfwqecdwhjvgwuqjcbhqwduchwndjwbhcnwjqdhcnwiujkxbhwndci' , font=('aerial' , 18 , 'bold'))

#canvas_text as score
score = canvas.create_text( 340 , 20 , text='SCORE : 0' , font=('impact' , 15 , 'normal'))

#buttons setup 
right_release = PhotoImage(file='right.png')
wrong_release = PhotoImage(file='wrong.png')
right_pressed = PhotoImage(file='right_pressed.png')
wrong_pressed = PhotoImage(file='Wrong_pressed.png')

right_but = ImageButton(300 , 470 , right_release , right_pressed , right)
wrong_but = ImageButton(100 , 470 , wrong_release ,wrong_pressed  , wrong)

'''
To run programme
'''
next_question()
window.mainloop()