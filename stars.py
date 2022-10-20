from turtle import Turtle
from random import randint

speed = 2
stretch_len = 0.1
stretch_wid = 0.1
h = 270
minpos = -500
maxpos = 500
num = 120


class Stars():

    def __init__(self):
        self.stars = []
        self.speed = speed

        for i in range(num):
            self.newstar()


    def newstar(self):
        star = Turtle(shape='circle')
        star.penup()
        star.shapesize(stretch_len, stretch_wid)
        star.color('lightyellow')
        star.setposition(randint(minpos, maxpos), randint(minpos, maxpos))
        star.setheading(h)
        self.stars.append(star)


    def move(self):
        for star in self.stars:
            star.forward(self.speed)
            if star.ycor() < minpos:
                star.setposition(star.xcor(), maxpos)
