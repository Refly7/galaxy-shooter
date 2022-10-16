import turtle

allbullets = []

class Missiles(turtle.Turtle):

    def __init__(self, x, y, b, c):
        turtle.Turtle.__init__(self)

        self.shape      ('circle')
        self.penup      ()
        self.color      (c)
        self.shapesize  (stretch_len = 0.5, stretch_wid = 0.5)
        self.setheading (90 * b)
        self.setposition(x, y)
        allbullets.append(self)


    def move(self):
        self.forward(15)
        
        if -505 > self.ycor() > 505:
            self.erase()


    def collision(self, obj):
        if self.distance(obj) < 20:
            self.erase()
            obj.hp -= 1
            return 1
        return 0

    
    def erase(self):
        allbullets.pop(allbullets.index(self))
        self.hideturtle()