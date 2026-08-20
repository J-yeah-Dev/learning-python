import time
from turtle import Turtle, Screen

from scoreboard import Scoreboard
from food import Food
from  snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #detect food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with walls
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.new_snake[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()