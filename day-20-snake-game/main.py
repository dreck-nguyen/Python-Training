from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game !!!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #     Detection the collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()
    #     Detection the collisions with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.reset()
        snake.reset()

    #     Detection the collisions with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreBoard.reset()
            snake.reset()

screen.exitonclick()
