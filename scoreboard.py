from turtle import Turtle

FONT = ("Arial", 22, "bold")
ALING = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Tu puntaje es: {self.score}", font=FONT, align=ALING)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Perdiste!!!, Juego Terminado", font=FONT, align=ALING)
