from turtle import Turtle
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.new_snake = []
        self.create_snake()
        self.head= self.new_snake[0]


    def create_snake(self):
        for index in range(0, 3):
            position = -20 * index, 0
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.new_snake.append(snake)

    def extend(self):
        self.add_segment(self.new_snake[-1].position())

    def reset(self):
        for seg in self.new_snake:
            seg.goto(900,900)
        self.new_snake.clear()
        self.create_snake()
        self.head = self.new_snake[0]

    def move(self):
        for seg_num in range(len(self.new_snake) - 1, 0, -1):
            new_x = self.new_snake[seg_num - 1].xcor()
            new_y = self.new_snake[seg_num - 1].ycor()
            self.new_snake[seg_num].goto(new_x, new_y)
        self.new_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

