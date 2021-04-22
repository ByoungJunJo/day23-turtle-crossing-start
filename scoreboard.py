from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # self.color("black")
        self.goto(-260, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL: {self.level}", move=False, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)

