from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('Black')
screen.title("My Snake Game")
screen.tracer(0)

border = Turtle()
border.color('yellow')
border.hideturtle()
border.penup()
border.goto(-290,-290)
border.pendown()

border.forward(580)
border.left(90)  
border.forward(560)
border.left(90) 
border.forward(580)
border.left(90)
border.forward(560)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # Scoreboard
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        snake.reset()
        # if scoreboard.score > high_score:
        scoreboard.reset_high_score()


    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset_high_score()


# screen.exitonclick()