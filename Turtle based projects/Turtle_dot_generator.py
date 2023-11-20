from turtle import Screen, Turtle, dot, setposition
from random import choice, randint, seed

color =  [ "red", "blue", "green", "yellow", "purple", "orange", 'cyan', "black" ]

turtle = Turtle()

turtle.speed(300)
turtle.hideturtle()

def position(length_of_side:int):
    digonal = (length_of_side)*(2**(1/2))
    turtle.penup()
    turtle.setheading(225)
    turtle.forward(round(digonal)/2)
    turtle.setheading(0)

def dots_in_line(gap,no_dots,size):
    for i in range (no_dots-1):
        Color = choice(color)
        turtle.dot(size,Color)
        turtle.forward(gap)
    turtle.dot(size)

def new_line(length_of_side , gap):
    turtle.left(90)
    turtle.forward(gap)
    turtle.left(90)
    turtle.forward(length_of_side - gap)
    turtle.left(180)
    


def dots(no_dots , length_of_side,size):
    gap = length_of_side/no_dots
    position(length_of_side)
    for i in range (no_dots):
        dots_in_line(gap,no_dots,size)
        new_line(length_of_side,gap)

dots(30,300,10)

screen = Screen()
screen.exitonclick()

