from tkinter import *
from main import SubTranslator
from tkinter import messagebox
import subprocess
import sys



PATH = r'C:\\Program Files (x86)\\IronPython 2.7\\Lib'
sys.path.append(PATH)

root = Tk()
root.title('SUB-TRANSLATOR')
root.geometry('400x200')


'''
Function
'''


def load_file():
    
    translate_but.config(state=DISABLED)
    path = file_path_entry.get()
    

    file_name = (path.split("\\"))[-1]
    file_name = 'J:\PYTHON CODES\PEOJECTS\Subtitle translator\Translated SubFile\MR.'+ file_name

    if len(path) == 0 :
        messagebox.showerror(title='Error' , message='Please enter file path with name')
        translate_but.config(state=ACTIVE)

    else:
        try :
            with open(path) as test:
                pass 

        except:
            messagebox.showerror(title='Error' , message='file path is not valid')
            file_path_entry.delete(0 , END)
            translate_but.config(state=ACTIVE)
        
        else :
            loading_label.config(text='READING FILE')
            translator = SubTranslator(path)
            
            
            reset_but.config(state=ACTIVE)
            open_folder_but.config(state=ACTIVE)
            loading_label.config(text='FILE SAVED')

def open_folder():
    subprocess.Popen('explorer "J:\PYTHON CODES\PEOJECTS\Subtitle translator\Translated SubFile"')
  
def reset():
    translate_but.config(state=ACTIVE)
    loading_label.config(text='NOT INITIATED')
    open_folder_but.config(state=DISABLED)
    reset_but.config(state=DISABLED)
    file_path_entry.delete(0 , END)

'''
UI 
'''

heading = Label(text='SUB-TRANSLATOR' , font=('Robot' , 20 , 'bold'))
heading.place(anchor=CENTER , x=200 , y=30)

heading2 = Label(text='MARATHI' , font=('Segoe UI' , 10 , 'bold'))
heading2.place(anchor=CENTER , x=200 , y=55)

file_path_entry = Entry(width=30 ,border=0 , bg='light grey')
file_path_entry.focus()
file_path_entry.place(anchor=CENTER , x=130 , y=100)

translate_but = Button(text='TRANSLATE' , width=18 ,font=('aerial' , 8 , 'bold') , command=load_file)
translate_but.place(anchor=CENTER , x=310 , y=99)

loading_label = Label(text='NOT INITIATED' , font=('Segoe UI' , 13 , 'bold' ))
loading_label.place(anchor=CENTER , x=200 , y=130)

open_folder_but = Button(text='OPEN FOLDER' , width=18 ,font=('aerial' , 8 , 'bold'),state=DISABLED , command=open_folder)
open_folder_but.place(anchor=CENTER , x=125 , y=180)

reset_but = Button(text='RESET' , width=18 ,font=('aerial' , 8 , 'bold'),state=DISABLED , command=reset )
reset_but.place(anchor=CENTER , x=285 , y=180)

root.mainloop()