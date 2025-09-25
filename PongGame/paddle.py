from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)

        self.y = position[1]

        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def Up(self):
        if self.ycor() > 250:
            return
        self.y += 20
        self.goto(self.xcor(), self.y)

    def Down(self):
        if self.ycor() < -230:
            return
        self.y -= 20
        self.goto(self.xcor(), self.y)