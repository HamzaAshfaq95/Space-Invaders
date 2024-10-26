from turtle import Turtle

class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("red")
        self.shapesize(2, 2)
        self.penup()
        self.setheading(90)
        self.goto(0, -320)

    def move_right(self):
        new_x = self.xcor() + 10
        if not self.xcor() > 367:
            self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 10
        if not self.xcor() < -370:
            self.goto(new_x, self.ycor())