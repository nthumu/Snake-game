from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
score = ScoreBoard()


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    screen.listen()
    screen.onkey(snake.snake_up, "Up")
    screen.onkey(snake.snake_down, "Down")
    screen.onkey(snake.snake_left, "Left")
    screen.onkey(snake.snake_right, "Right")

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()
