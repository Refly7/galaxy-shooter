from turtle import Turtle
from random import randint

class Stars(Turtle):

    def __init__(self):
        self.stars = []
        self.speed = 2

        for i in range(120):
            self.newstar()


    def newstar(self):
        star = Turtle(shape='circle')
        star.penup()
        star.shapesize(stretch_len = 0.1, stretch_wid = 0.1)
        star.color('lightyellow')
        star.setposition(randint(-500, 500),randint(-500, 500))
        star.setheading(270)
        self.stars.append(star)


    def move(self):
        for star in self.stars:
            star.forward(self.speed)
            if star.ycor() < -500:
                star.setposition(star.xcor(), 500)