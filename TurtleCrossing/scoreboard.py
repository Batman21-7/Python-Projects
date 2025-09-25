from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)

        self.level = 0
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f'Level is: {self.level}', align='left', font=('Times New Roman', 20, 'normal'))

    def game_over(self):
        self.home()
        self.write('Game Over', align='center', font=('Times New Roman', 30, 'normal'))
