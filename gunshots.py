from turtle import Turtle

class GunShots:
    def __init__(self):
        self.gunshots = []

    def create_gunshot(self, x, y):
        shot = Turtle("square")
        shot.shapesize(0.6, 0.1)
        shot.color("red")
        shot.penup()
        shot.goto(x, y)
        self.gunshots.append(shot)

    def move(self):
        for shot in self.gunshots:
            shot.sety(shot.ycor() + 15)