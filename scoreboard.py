from turtle import Turtle

ALIGNMENT = "center"
BOARDALIGN = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-295, 180)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=BOARDALIGN, font=15)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER !!!!", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
