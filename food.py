from turtle import Turtle
from random import randint

# Class to create food on screen
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize()
        self.speed('fastest')
        self.refresh()

# function which refresh food at random position on screen
    def refresh(self):
        random_x = randint(-280,281)
        random_y = randint(-280,250)
        self.goto(random_x, random_y)