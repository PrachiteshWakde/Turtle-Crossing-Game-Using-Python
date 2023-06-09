import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def start(self):
        self.setpos(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

