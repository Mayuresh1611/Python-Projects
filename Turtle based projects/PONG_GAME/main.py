# imports of required modules 
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Devider , Score

# setups the screen 
screen = Screen()
screen.setup( width = 800 , height = 600 )
screen.bgcolor("black")
screen.tracer(0)

# setups the paddle of game
l_paddle = Paddle(-360,0)
r_paddle = Paddle(360,0)

#setups the scoreboard
score = Devider()
player1_l = Score(-60 , 210)
player2_r = Score(60 , 210)

# setups the ball
ball = Ball()

# setup to control the paddles 
screen.listen()
screen.onkey(l_paddle.up , 'w')
screen.onkey(r_paddle.up , 'Up')
screen.onkey(l_paddle.down , 's')
screen.onkey(r_paddle.down , 'Down')


# game mechanics
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    
    # detects if ball is colliding to upper and down wall
    if ball.ycor() > 280 or  ball.ycor() < -280:
        ball.bounce_y()
    
    # detects if ball hits on paddle and chages the direction accordingly
    if ball.xcor() > 340 and ball.distance(r_paddle) < 55 or ball.xcor() < -340 and ball.distance(l_paddle) < 55:
        ball.bounce_x()
    
    #detects if ball is missed by player_2 and increases the score of player_1
    if ball.xcor() > 390:
        player1_l.score_inc()
        ball.reposition()

    #detects if ball is missed by player_1 and increases the score of player_2
    if ball.xcor() < -390:
        player2_r.score_inc()
        ball.reposition()
        
        
screen.exitonclick()