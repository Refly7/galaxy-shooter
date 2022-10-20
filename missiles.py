import turtle

allbullets = []
stretch_len = 0.5
stretch_wid = 0.5
max = 505
dis_to_bullet = 20
dmg = 1


class Missiles(turtle.Turtle):

    def __init__(self, x, y, b, c):
        turtle.Turtle.__init__(self)

        self.shape      ('circle')
        self.penup      ()
        self.color      (c)
        self.shapesize  (stretch_len, stretch_wid)
        self.setheading (b)
        self.setposition(x, y)
        allbullets.append(self)


    def move(self):
        self.forward(15)
        
        if -max > self.ycor() > max:
            self.erase()


    def collision(self, obj):
        if self.distance(obj) < dis_to_bullet:
            self.erase()
            obj.hp -= dmg

    
    def erase(self):
        allbullets.pop(allbullets.index(self))
        self.hideturtle()
