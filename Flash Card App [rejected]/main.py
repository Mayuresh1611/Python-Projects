from tkinter import *
from button import ImageButton, ToggleButton
from pandas import *
from time import sleep

running = True
index = 0

window = Tk('Flash Cards' )
window.geometry('700x500')
window.title('Flash Cards')

'''images'''
card_front = PhotoImage(file='Card Front.png')
card_back = PhotoImage(file= 'Card Back.png')

wrong_pressed = PhotoImage(file='Wrong_pressed.png')
wrong_released = PhotoImage(file='Wrong_released.png')

right_pressed = PhotoImage(file='right_pressed.png')
right_released = PhotoImage(file='right_released.png')

flip_front = PhotoImage(file='flip front.png')
flip_back = PhotoImage(file='flip back.png')

'''canvas setup'''
canvas = Canvas(height=500 , width=700 )
canvas.place(x=350 , y=250 , anchor=CENTER)

card = canvas.create_image( 350 , 250 , image=card_front )

'''labels / words setup'''
heading = canvas.create_text(355 , 95 , text='' , font=('aerial' , 40 , 'bold'))
content = canvas.create_text(355 , 175 , text='' , font=('aerial' , 25 , 'italic'))


'''Functions setup'''

data = read_csv('japanese.csv')
jp_kanji = data['kanji'].to_list()

# Cards flipping function

# managing Contents of the card 

def front_content(kanji):
    line = data[data['kanji'] == kanji]
    canvas.itemconfig(heading , text=kanji )
    canvas.itemconfig(content , text=(line.pronounciation.item()))

def back_content(kanji):
    line = data[data['kanji'] == kanji]
    canvas.itemconfig(heading , text=(line.pronounciation.item()) )
    canvas.itemconfig(content , text=(line.meaning.item()))

def front_card():
    front_content('男')
    canvas.itemconfig(card , image=card_front)

def back_card():
    back_content('男')
    canvas.itemconfig(card , image=card_back)

def frequecncy_check(kanji):
    line = data[data['kanji'] == kanji]
    frequency = line.frequency.item()

    if frequency == 'frequent':
        return 2
    elif frequency == 'normal':
        return 0
    else:
        return 9
'''Button Setup'''

flip = ToggleButton(570 , 330 , flip_front , flip_back , back_card , front_card)
wrong = ImageButton(200 , 425 , wrong_released , wrong_pressed )
right = ImageButton(500 , 425 , right_released , right_pressed )


window.mainloop()
