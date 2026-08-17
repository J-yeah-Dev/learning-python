import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40,-10,20,50,80]
all_turtles = []

if user_bet:
    if user_bet in colors:
        is_race_true = True
    else:
        is_race_true = False
        print("That is not a valid color. Please retry")

for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240,y_position[turtle_index])
    all_turtles.append(new_turtle)


while is_race_true:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_true = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won! The {winning_color} turtle is the winner")
            else:
                print(f"you have lost! The {winning_color} turtle is the winner")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()
