from turtle import Turtle
MOUVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.starting_position = [(0 , 0), (-20, 0), (-40 , 0)]
        self.all_snake = []
        self.create_snake()

    def create_snake(self):
        for position in self.starting_position:
            self.add_snake(position)

    def add_snake(self, position):        
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_snake.append(snake)
        
    def extend(self):
        self.add_snake(self.all_snake[-1].position())
        
        
    def move(self):
        for snake_num in range(len(self.all_snake) - 1 , 0 , -1):
            new_x = self.all_snake[snake_num - 1].xcor()
            new_y = self.all_snake[snake_num - 1].ycor()
            self.all_snake[snake_num].goto(new_x , new_y)

        self.all_snake[0].forward(MOUVE_DISTANCE)


    def up(self):
        if self.all_snake[0].heading() != DOWN:
            self.all_snake[0].setheading(UP)
        
    def down(self):
        if self.all_snake[0].heading() != UP:
            self.all_snake[0].setheading(DOWN)
        
    def left(self):
        if self.all_snake[0].heading() != RIGHT:
            self.all_snake[0].setheading(LEFT)
        
    def right(self):
        if self.all_snake[0].heading() != LEFT:
            self.all_snake[0].setheading(RIGHT)
            
            
    def reset(self):
        for snake in self.all_snake:
            snake.goto(1000 , 1000)
        self.all_snake.clear()      
        self.create_snake()  