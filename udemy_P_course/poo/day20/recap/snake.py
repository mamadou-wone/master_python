from turtle import Turtle
STARTING_POSITION = [(0 , 0) , (-20 , 0), (-40 , 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    all_snake = []
    def __init__(self):
        for position in STARTING_POSITION:
            self.create_snake(position)
    
    
    def create_snake(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_snake.append(snake)
     
    def extend(self):
        self.create_snake(self.all_snake[-1].position())
            
    def move(self):
        for snake_num in range(len(self.all_snake) - 1 , 0 , -1):
            new_x = self.all_snake[snake_num - 1].xcor()
            new_y = self.all_snake[snake_num - 1].ycor()
            self.all_snake[snake_num].goto(new_x , new_y)
        self.all_snake[0].forward(MOVE)    
               
    def Up(self):
        if self.all_snake[0].heading() != DOWN: 
           self.all_snake[0].setheading(UP)
        
    def Down(self):
        if self.all_snake[0].heading() != UP: 
            self.all_snake[0].setheading(DOWN)    
    
    def Left(self):
        if self.all_snake[0].heading() != RIGHT: 
            self.all_snake[0].setheading(LEFT)
    
    def Right(self):
        if self.all_snake[0].heading() != LEFT: 
            self.all_snake[0].setheading(RIGHT)