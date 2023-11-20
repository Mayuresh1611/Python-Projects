# tkinter import
from tkinter import * 

# some constants
reps = 0
PAUSE = False
TIME  = ''
tick = '✔'
num = 0

#-----------------------------------------------------(GUI SETUP)-------------------------------------------------------#
# tkinter screen setup
screen = Tk()
screen.minsize(width=360 , height=450)
screen.title("POMODORO")
screen.config(padx= 0 , pady= 0)

# Canvas setup with background image
canvas = Canvas(width=360 , height=450 , bg='white')
tomato_img = PhotoImage(file='Pomodoro_tomato.png')
image = canvas.create_image(180 ,225 , image= tomato_img)
canvas.place(x=0 , y=0)

#-----------------------------------------------------(WIDGET SETUP)-------------------------------------------------------#
# LABEL text on canvas
heading = canvas.create_text(185,398,text='TIMER' , fill='black', font=('impact',20,'normal'))
# Ticks on canvas
ticks = canvas.create_text(185,363.5,text= ' ' , fill='green', font=('impact',13,'normal'))
# timer text
timer = canvas.create_text(185 , 197.5 ,text=f'00:00' ,fill='black', font=('impact',32,'normal'))


#-----------------------------------------------------(TIMER SETUP)-------------------------------------------------------#

# starts the timer upon access
def start_timer():
    global reps , num
    reps += 1
    
    start_button.config(command=UNpause)

    if reps % 6 == 0  :
        num = num + 1
        canvas.itemconfig(ticks , text= tick * num)
        countdown(20 * 60)
        canvas.itemconfig(heading , text= 'REST')

    elif reps % 2 != 0:
        countdown(25 * 60)
        canvas.itemconfig(heading , text= 'WORK')

    elif reps % 2 == 0:
        num = num + 1
        canvas.itemconfig(ticks , text= tick * num)
        countdown(5 * 60)    
        canvas.itemconfig(heading , text= 'BREAK')

# Countdown function
def countdown(time):
    """Countdowns given interval of time 
    time must be in seconds"""
    min = time // 60
    sec = time % 60
    min1 = ''
    sec1 = ''

    if min < 10:
        min1 = 0
    if sec < 10:
        sec1 = 0

    if time >= 0:
    
        if PAUSE == False:
            canvas.itemconfig(timer , text= f'{min1}{min}:{sec1}{sec}')
            screen.after(10 , countdown ,time - 1 )

        elif PAUSE == True:
            global TIME
            TIME = time
            canvas.itemconfig(heading , text= 'PAUSED')
            
    else :
        start_timer()

# pauses the timer
def pause():
    global PAUSE
    PAUSE = True    

# resumes the timer
def UNpause():
    global PAUSE  , TIME
    PAUSE = False 
    countdown(TIME)
    global reps   
    if reps % 6 == 0  :
        canvas.itemconfig(heading , text= 'REST')

    elif reps % 2 != 0:
        canvas.itemconfig(heading , text= 'WORK')

    elif reps % 2 == 0:
        canvas.itemconfig(heading , text= 'BREAK')

#-----------------------------------------------------(BUTTONS)-------------------------------------------------------#

# buttons
start_png = PhotoImage(file='Start.png')
start_button = Button( text='START' ,image=start_png ,height=36 , width=80 ,command=start_timer, border=0,background='yellow')
start_button.place(x=60,y=373 , anchor='center')

stop_png = PhotoImage(file='Stop.png')
stop_button = Button( text='STOP' ,image=stop_png ,height=36 , width=80 , background='yellow', border=0 , command=pause)
stop_button.place(x=260,y=355)



screen.mainloop()