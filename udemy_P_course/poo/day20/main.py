from turtle import Screen
import  time
from snake import Snake
from food import Food
from score_board import ScoreBoard


screen = Screen()
screen.setup(width= 600, height = 600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_one = True

while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()    

    # Detect Colision with food
    if snake.all_snake[0].distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()

    # Detect colision with the wall
    if snake.all_snake[0].xcor() > 280 or snake.all_snake[0].xcor() < -280 or snake.all_snake[0].ycor() > 280 or snake.all_snake[0].ycor() < -280:
        game_is_one = False
        score.game_over()

    # Detect collision with fail
    for segment in snake.all_snake[1:]:
        if snake.all_snake[0].distance(segment) < 10:         
            game_is_one = False
            score.game_over()
    
screen.exitonclick()