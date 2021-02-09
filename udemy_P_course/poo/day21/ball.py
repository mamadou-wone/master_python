from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        
    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x , new_y)

    def reset_ball(self):
        self.goto(0 , 0)
        self.bounce_x()
        self.move_speed = 0.1
        
        
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
        # self.y_move -= 10
        
    def bounce_x(self):
        self.x_move *= -1
        # self.x_move -= 10    
        
        