
from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        x = 0.0
        for _ in range(5):
            tim = Turtle("square")
            tim.penup()
            tim.color("white")
            tim.goto(x, 0.0)
            self.segments.append(tim)
            x -= 20.0

    def move(self):
        for position in range(len(self.segments) - 1, 0, -1):
            self.segments[position].goto(self.segments[position - 1].xcor(), self.segments[position - 1].ycor())
        self.segments[0].forward(20)

    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def add_segment(self):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(self.segments[-1].position())
        self.segments.append(tim)

    def reset_snake(self):

        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()


