from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

screen = Screen()
screen.setup(800, 600)      
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


l_paddle = Paddle((-350 , 0))
r_paddle = Paddle((350 , 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()
    
    # Detect colision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce_y()
        ball.speed("fastest")
    # Detect colision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed("fastest")


    # Detect when the ball goes out of bounds
    if ball.xcor() > 380: 
        ball.reset_ball()
        score.l_score += 1
        score.reset()
        score.show_score()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_score += 1
        score.reset()
        score.show_score()









screen.exitonclick()