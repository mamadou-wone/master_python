import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()        

screen.listen()
screen.onkey(player.move_player, "Up")


game_is_on = True
index = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car_move()
    index += 1
    if index % 6 == 0:
        car.generate_car()

    
    # Detect colision with car
    for item in car.car_bank:
        if item.distance(player) < 20:
            game_is_on = False
            score.game_over()
    
    # Detect when player finish the y_line
    if player.check_finish_line():
        player.star_position()
        car.increase_move()
        score.increase_score()


screen.exitonclick()    