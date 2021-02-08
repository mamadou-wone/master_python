from turtle import Turtle, Screen
from snake import Snake
import time
from fooo import Food
from score_board import ScorBoard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake GAME")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
score_board = ScorBoard()



screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect Colision with the food
    if snake.all_snake[0].distance(food) < 15:
        snake.extend()
        score_board.update_score()
        food.gen_food()

    # Detect colision with the wall
    if snake.all_snake[0].xcor() > 280 or snake.all_snake[0].xcor() < -280 or snake.all_snake[0].ycor() > 280 or snake.all_snake[0].ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # Detect colision with the snake body
    for segment in snake.all_snake[1:]:
        if snake.all_snake[0].distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
        



screen.exitonclick()