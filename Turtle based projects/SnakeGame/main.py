# Imports of important modules
from turtle import Screen 
from snake import Snake
from food import Food
from score import Score
from time import sleep

# setups the scree to run snake game
screen = Screen()
screen.setup(width=600,height=620)
screen.bgcolor("black")
screen.title('SNAKE GAME')
screen.tracer(0)

# initiates the required classes
snake = Snake()
snake.create()
score = Score()
food = Food()

# to control the snake
screen.listen()
screen.onkey(snake.left , 'a')
screen.onkey(snake.right , 'd')
screen.onkey(snake.up ,'w')
screen.onkey(snake.down , 's')


# this runs the game using the methods 
game_is_on  = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    """ when head of snake eats the food then 
    score incriminates with 1
    snake adds 1 more segment 
    food changes it's position"""

    if snake.head.distance(food) < 15:
        score.score_adder()
        snake.add_seg()
        food.eaten()

    # gives out head co-ordinates
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    
    """if head is out world range then snake game ends"""
    if x_cor > 300 or x_cor < -300 or y_cor > 300 or y_cor < -300:
        sleep(0.3)
        score.high_score()
        score.end_score()
        snake.clear_snake()
        snake.create()
        score = Score()
        

    """if head is colliding ith any of the segment of snake itself then
    game ends"""
    for i in range(len(snake.segments)-1,2,-1) :
        if snake.head.distance(snake.segments[i]) < 1:
            sleep(0.3)
            score.high_score()
            score.end_score()
            
            snake.clear_snake()
            snake.create()
            score = Score()
            break
        
# exits the game       
screen.exitonclick()


