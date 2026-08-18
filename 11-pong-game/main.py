from turtle import Turtle, Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard =Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor()> 290 or ball.ycor()< -290:
        ball.bounce_y()

    #detect collision with paddle
    if ((ball.xcor()> 330 and ball.distance(r_paddle)< 40) or (ball.xcor()<-330 and ball.distance(l_paddle)< 40)):
        ball.bounce_x()

    #detect ball missing r_paddle
    if (ball.xcor()> 390):
        # game_is_on = False
        ball.reset_position()
        scoreboard.l_point()

    #detect ball missing l_paddle
    if (ball.xcor()<-390):
        # game_is_on = False
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()