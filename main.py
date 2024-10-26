import time
from turtle import *
from spaceship import SpaceShip
from gunshots import GunShots
from hurdles import Hurdles

screen = Screen()
screen.setup(800, 700)
screen.title("Space Invaders")
screen.tracer(0)

SS = SpaceShip()
gunshots = GunShots()
hurdles = Hurdles()

def create_fire():
    gunshots.create_gunshot(SS.xcor(), SS.ycor())

def collision():
    for hurdle in hurdles.hurdles:
        for fire in gunshots.gunshots:
            if hurdle.distance(fire) < 20:
                hurdle.goto(1000, 1000)
                fire.goto(1000, 1000)

screen.listen()
screen.onkey(SS.move_right, "Right")
screen.onkey(SS.move_left, "Left")
screen.onkey(create_fire, "space")

while True:
    time.sleep(0.1)
    gunshots.move()
    hurdles.move_hurdles()
    collision()
    screen.update()