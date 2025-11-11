from turtle import Turtle

ALING_ = "center"
FONT_A = "Arial"
TYPE_LETTER = "normal"

class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            try:
                with open("data.txt", mode="r") as data_file:
                    self.high_score = int(data_file.read())
            except (FileNotFoundError, ValueError):
                self.high_score = 0
            self.penup()
            self.color("white")
            self.goto(0, 265    )
            self.hideturtle()
            self.update_score()


        def update_score(self):
            self.clear()
            self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALING_, font=(FONT_A, 24, TYPE_LETTER))

        def reset_score(self):
            if self.score > self.high_score:
                self.high_score = self.score
                with open("data.txt", mode="w") as data_file:
                    data_file.write(str(self.high_score))
            self.score = 0
            self.update_score()

        def increase_score(self):
            self.score += 1
            self.update_score()

        #def game_over(self):
        #    self.goto(0, 0)
        #   self.write("Game Over", align=ALING_, font=(FONT_A, 24, TYPE_LETTER))