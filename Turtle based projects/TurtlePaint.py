from turtle import _Screen, Screen, Turtle, back

popy = Turtle('turtle')
size = 2

def forward():
    popy.forward(20)
def backward():
    popy.back(20)
def left():
    popy.left(30)
def right():
    popy.right(30)
def clear():
    popy.clear()
def pen_size():
    popy.pensize(size+10)
def pen_up():
    popy.penup()
def pen_down():
    popy.pendown()

screen = Screen()
screen.listen( )
screen.onkey(forward,'w')
screen.onkey(left,'a')
screen.onkey(right,'d')
screen.onkey(back,'s')
screen.onkey(clear , 'c')
screen.onkey(pen_up,'Up')
screen.onkey(pen_down,'Down')
screen.onkey(pen_size,'+')

screen.exitonclick()
 