from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Times New Roman", 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score is: {self.score}     High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update_scoreboard()
