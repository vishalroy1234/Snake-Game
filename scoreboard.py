
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        self.highest_score = int(self.get_highest_score())
        self.speed("fastest")
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.refresh()

    def get_highest_score(self):
        with open('highest_score.txt') as file:
            return file.read()

    def refresh(self):
        self.clear()
        self.write(f"Score:{self.score}   Highest-score:{self.highest_score}", False, "center", ("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.refresh()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, "center", ("Arial", 14, "normal"))
    #     self.goto(0, 50)
    #     self.write(f"Final Score: {self.score}", False, "center", ("Arial", 14, "normal"))

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('highest_score.txt', 'w') as file:
                file.write(str(self.highest_score))

        self.score = 0
        self.refresh()
