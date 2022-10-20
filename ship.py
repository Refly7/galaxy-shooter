from missiles import Missiles
import turtle

hp = 3
xpos = 0
ypos = -200
max = 480
up = 90
down = 270
right = 0
left = 180
speed = 8
dis_to_bullet = 20

turtle.register_shape("ship.gif")

class Ship(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, shape="ship.gif")
        self.penup()
        self.setposition(xpos, ypos)
        self.hp = hp
        self.speed('fastest')

    def up(self):
        if self.ycor() < max:
            self.setheading(up)
            self.forward(speed)
        
    def down(self):
        if self.ycor() > -max:
            self.setheading(down)
            self.forward(speed)

    def right(self):
        if self.xcor() < max:
            self.setheading(right)
            self.forward(speed)

    def left(self):
        if self.xcor() > -max:
            self.setheading(left)
            self.forward(speed)

    def shoots(self):
        Missiles(self.xcor(), self.ycor() + dis_to_bullet, up, 'goldenrod')
