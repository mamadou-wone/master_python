COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.car_bank = []
        self.generate_car()
        self.move_speed = STARTING_MOVE_DISTANCE


    def generate_car(self):
        new_x  = random.randint(290, 300)
        new_y  = random.randint(-240, 270)
        color = random.choice(COLORS)
        car = Turtle("square")
        car.penup()
        car.color(color)
        car.goto(new_x, new_y)
        car.shapesize(stretch_wid=1 , stretch_len=2)
        car.setheading(180)
        self.car_bank.append(car)

          
    def car_move(self):
        for car in self.car_bank:
            car.forward(self.move_speed)        
        
    def increase_move(self):
        self.move_speed += MOVE_INCREMENT
            