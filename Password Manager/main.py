#==================================================================================================================#
#|                                              PASSWORD MANAGER                                                  |#
#==================================================================================================================#


import json
from tkinter import *
from tkinter import messagebox
from random import random , choice, sample 


#-------------------------------------------(CHARECTERS FOR PASSWORD)----------------------------------------------#

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']
#-----------------------------------------------------(GUI)--------------------------------------------------------#

window = Tk()
window.minsize(width= 600 , height= 400)

mypass_img = PhotoImage(file='Mypass.png')
canvas = Canvas(width= 600 , height= 400 , background='white')
canvas.create_image(300 ,110 , image= mypass_img)
canvas.place(anchor='center' , x= 300 , y=200)

#---------------------------------------------------(SAVE PASSWORD)-------------------------------------------------------#

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_info = {website :{
        'Email': email,
        'Password': password
    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("oops !", "Please fill the required fields") 

    else:
        if (messagebox.askokcancel(f"{website}",  f"EMAIL: {email}\nPASSWORD:  <{password}>\n\n PROCEED?")):
            with open('Passkeys.json' , 'r') as file :
                info = json.load(file)
                info.update(new_info)
            with open('Passkeys.json' , 'w') as file :
                json.dump(info ,file  ,indent= 4 )
                  
            website_input.delete(0 , END)
            password_input.delete(0 , END)
            

#----------------------------------------------(PASSWORD GENRATOR)--------------------------------------------------------#

def password_gernerator():
    password_input.delete(0,END)
    password = [choice(LOCASE_CHARACTERS) for num in range(4)]
    pass_key = ''
    
    for i in range(2):
        password.append(choice(UPCASE_CHARACTERS))
        password.append(choice(DIGITS))
        password.append(choice(SYMBOLS))

    new_password = sample(password , len(password))

    for i in new_password:
        pass_key += i
    
    password_input.insert(0,f'{pass_key}')
    


#----------------------------------------------(SEARCH INFO)---------------------------------------------------------#
    
def search():
    website = website_input.get()

    with open('Passkeys.json' , 'r') as file:
        data = json.load(file) 

    if website in data:
        email = (data[website]['Email'])
        password = (data[website]['Password']) 
    else:
        messagebox.showerror("oops !", f"Website with name {website} not found !") 
        
    try:
        email
        password

    except:
        pass

    else:
        if (messagebox.askokcancel(f"{website}",  f"EMAIL: {email}\nPASSWORD:  <{password}>\n\n Press OK! to fill it!")):
            email_input.delete(0 , END)
            email_input.insert(0 ,email)
            password_input.insert(0 , password)    


#--------------------------------------------------(UI Setup)--------------------------------------------------------#

# Labels

website_l = canvas.create_text(130, 240,text='Website :' , fill='black' , font=( 'aerial',10 ,'bold'))
email_l = canvas.create_text(130, 270,text='Email/Username :' , fill='black' , font=( 'aerial',10 ,'bold'))
password_l = canvas.create_text(130, 300,text='Password :' , fill='black' , font=( 'aerial',10 ,'bold'))

# Buttons

'''Generate button'''
generate_but = Button(text='Generate'  ,width= 19 ,height=1, font=( 'aerial',9 ,'bold') , command= password_gernerator)
generate_but.place(anchor='center' , x= 428 , y=298 )

'''ADD button'''
add_but = Button(text='ADD' ,width= 42 ,height=1, font=( 'aerial',9 ,'bold') , command=save)
add_but.place(anchor='center' , x= 348, y=330 )

'''Search button'''
search_but = Button(text='Search'  ,width= 19 ,height=1, font=( 'aerial',9 ,'bold') , command=search)
search_but.place(anchor='center' , x= 428 , y=240 )


# Entries

'''Website input'''
website_input = Entry(width= 25 , background='light grey' , font=( 'aerial',8 ,'bold') )
website_input.focus()
website_input.place(anchor='center' , x= 275 , y=240 )

'''Email/Username input'''
email_input = Entry( width=50 , background='light grey' , font=( 'aerial',8 ,'bold'))
email_input.insert(END , 'mayurus1611@gmail.com')
email_input.place(anchor='center' , x= 350 , y=268 )

'''password input'''
password_input = Entry(width=25 , background='light grey' , font=( 'aerial',8 ,'bold'))
password_input.place(anchor='center' , x= 275 , y=300 )



window.mainloop()