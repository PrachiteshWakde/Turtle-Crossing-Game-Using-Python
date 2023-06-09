import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update()


    def update(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)


