from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial',20,'normal')

# Scoreboard class which controls the scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)   
        self.update_scoreboard()    

# function which updates the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , move = False, align=ALIGNMENT, font=FONT)

# function which reset the highscore
    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
      
# function which increment the score
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    