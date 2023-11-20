# some required imports 
from turtle import Screen
from time import sleep
from cars import Cars
from turtle_crosser import WalkingTurtle
from scoreboard import Levels

# screen setup
screen = Screen()
screen.title('CROSS THE ROAD WITH TURTLE')
screen.setup(height=600 , width= 600)
screen.tracer(0)

# Walking turtle setup
turtle = WalkingTurtle()

# current level setup
levels = Levels()

# spawns 4 cars 
for i in range (4):
    car = Cars()

# Controlling turtle (moving turtle forward using keys)
screen.listen()
screen.onkey(turtle.move_forward,'w')


# Setup of game mechanics
x = 0
speed = 0
game_is_on = True
while game_is_on :
    
    # Detects if turtle reached the top of screen
    if turtle.ycor() > 280:
        """Increases speed of cars by 5"""
        speed += 5

        """Increases no. of level """
        levels.level_inc()

        """brings turtle back to bottom of screen"""
        turtle.reposition()

    # Moves cars on road and detects collision with turtle 
    for i in car.cars:
        ''' moves each car forward by it's given speed'''
        i.move()
        i.speed_inc(speed)

        '''checks if the distance between car and turtle is less than 30 (checks if turtle hits the car)'''
        if i.distance(turtle) < 30:
            '''Shows game over message'''
            levels.game_over()

            '''ends the while loop'''
            game_is_on = False
    
    # Spawns a car every third loop
    x += 1
    if x == 3:
        x = 0
        car = Cars()
    
    # updates the screen by 0.1 sec
    sleep(0.1)
    screen.update()
    
# exits    
screen.exitonclick()