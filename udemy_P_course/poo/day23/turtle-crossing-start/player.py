STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()


    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
        
        
    def move_player(self):
        self.forward(MOVE_DISTANCE)    
        
    
    def star_position(self):
        self.goto(STARTING_POSITION)
    
    def check_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
        