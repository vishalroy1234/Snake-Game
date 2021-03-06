from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("blue")
        self.penup()
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
