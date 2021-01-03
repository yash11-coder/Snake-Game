from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt",mode="w") as data:
                 data.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            with open("data.txt",mode="w") as data:
                 data.write(str(self.score))
        self.update_scoreboard()
