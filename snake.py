from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.speed("fastest")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake.append(new_turtle)

    def reset(self):
        for part in self.snake:
            part.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]


    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move_snake(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(20)

    def snake_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def snake_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def snake_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def snake_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
