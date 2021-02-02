
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if food.distance(snake.segments[0]) <= 15:
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) <= 10:
            scoreboard.update_highest_score()
            snake.reset_snake()
            break

    if snake.segments[0].xcor() >= 300 or snake.segments[0].ycor() >= 300\
            or snake.segments[0].xcor() <= -300 or snake.segments[0].ycor() <= -300:
        scoreboard.update_highest_score()
        snake.reset_snake()


screen.exitonclick()

