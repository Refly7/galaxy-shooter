import turtle
import os

os.chdir("C:\\Users\\Lenovo\\Desktop\\Mój Folder\\Python\\100 dni\\galaxiga")
turtle.register_shape("powerup.gif")

class PowerUp(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self, shape = "powerup.gif")

        self.penup      ()
        self.shapesize  (stretch_len = 0.5, stretch_wid = 0.5)
        self.setheading (270)
        self.setposition(x, y)


    def move(self):
        self.forward(5)
        
        if self.ycor() > -505:
            self.hideturtle()