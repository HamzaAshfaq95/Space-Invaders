from turtle import Turtle
import random

POSITIONS = [(-400, 320), (-360, 320), (-320, 320), (-280, 320), (-240, 320), (-200, 320), (-160, 320), (-120, 320), (-80, 320), (-40, 320), (0, 320), (40, 320), (80, 320), (120, 320), (160, 320), (200, 320),
             (-400, 280), (-360, 280), (-320, 280), (-280, 280), (-240, 280), (-200, 280), (-160, 280), (-120, 280), (-80, 280), (-40, 280), (0, 280), (40, 280), (80, 280), (120, 280), (160, 280), (200, 280),
             (-400, 240), (-360, 240), (-320, 240), (-280, 240), (-240, 240), (-200, 240), (-160, 240), (-120, 240), (-80, 240), (-40, 240), (0, 240), (40, 240), (80, 240), (120, 240), (160, 240), (200, 240),
             (-400, 200), (-360, 200), (-320, 200), (-280, 200), (-240, 200), (-200, 200), (-160, 200), (-120, 200), (-80, 200), (-40, 200), (0, 200), (40, 200), (80, 200), (120, 200), (160, 200), (200, 200)]
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "black", "pink", "cyan", "magenta"]

class Hurdles:
    def __init__(self):
        self.hurdles = []
        self.distance = 5
        self.create_hurdle()
        self.count = 10

    def create_hurdle(self):
        for pos in POSITIONS:
            hurdle = Turtle("circle")
            hurdle.color(random.choice(COLORS))
            hurdle.penup()
            hurdle.goto(pos)
            self.hurdles.append(hurdle)

    def move_hurdles(self):
        if self.count > 10:
            self.distance = -5
        elif self.count < -10:
            self.distance = 5
        else:
            self.distance = 5 if self.count >= 0 else -5

        for hurdle in self.hurdles:
            hurdle.setx(hurdle.xcor() + self.distance)

        self.count -= 1
        if abs(self.count) > 10:
            self.count = 10  # Reset count if it's out of bounds