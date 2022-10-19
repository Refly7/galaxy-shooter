from missiles import Missiles
import turtle
import os


os.chdir("C:\\Users\\Lenovo\\Desktop\\Mój Folder\\Python\\100 dni\\galaxiga")
turtle.register_shape("ship.gif")


class Ship(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, shape="ship.gif")
        self.penup()
        self.setposition(0, -200)
        self.hp = 3
        self.speed('fastest')

    def up(self):
        if self.ycor() < 480:
            self.setheading(90)
            self.forward(8)
        
    def down(self):
        if self.ycor() > -480:
            self.setheading(270)
            self.forward(8)

    def right(self):
        if self.xcor() < 480:
            self.setheading(0)
            self.forward(8)

    def left(self):
        if self.xcor() > -480:
            self.setheading(180)
            self.forward(8)

    def shoots(self):
        Missiles(self.xcor(), self.ycor() + 20, 90, 'goldenrod')
