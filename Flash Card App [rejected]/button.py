from tkinter import * 
is_on = False

class ImageButton(Button):
    
    def __init__(self , x_cor , y_cor , image1 , image2 , *functions):

        self = Button(image= image1 , bd=0 , relief='sunken')

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

class ToggleButton(Button):
    
    def __init__(self , x_cor , y_cor , image_1 , image_2 , function1 , function2):
        super().__init__()
        
        self.image_1 = image_1
        self.image_2 = image_2
        self.function1 = function1
        self.function2 = function2

        self = Button( image=image_1 , bd=0 , relief='sunken')

        def switch(_):
            global is_on
            print(is_on)
            if is_on:
                print(is_on)
                self.config(image=image_2 , command=function1)
                is_on = False
            else:
                print(is_on)
                self.config(image=image_1 , command=function2)
                is_on = True

        self.bind('<ButtonPress>' , switch)
        self.place(anchor=CENTER , x=x_cor , y=y_cor)

