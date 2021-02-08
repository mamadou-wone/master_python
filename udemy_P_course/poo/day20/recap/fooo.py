from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.gen_food()
        
        
    def gen_food(self):
        x = random.randint(-280 , 280)
        y = random.randint(-280 , 280)
        self.shape("circle")
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.goto(x , y)    
        