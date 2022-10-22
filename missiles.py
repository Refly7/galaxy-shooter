import turtle

allbullets = []
stretch_len = 0.5
stretch_wid = 0.5
max = 505
dis_to_bullet = 20
dis_to_bullet_boss = 60
dmg = 1
speed = 15
diraction = 270
lvl = 3
h = 90


class Missiles(turtle.Turtle):

    def __init__(self, x, y, c, b = diraction, speed = speed):
        turtle.Turtle.__init__(self)

        self.shape      ('circle')
        self.penup      ()
        self.color      (c)
        self.shapesize  (stretch_len, stretch_wid)
        self.setheading (b)
        self.speed = speed
        self.setposition(x, y)
        allbullets.append(self)


    def move(self):
        self.forward(self.speed)
        
        if -max > self.ycor() or self.ycor() > max:
            self.erase()


    def collision(self, obj):
        if self.distance(obj) < dis_to_bullet or obj.lvl == lvl and self.distance(obj) < dis_to_bullet_boss and self.heading() == h:
            self.erase()
            obj.hideturtle()
            obj.hp -= dmg
            return True

        return False

    
    def erase(self):
        allbullets.pop(allbullets.index(self))
        self.hideturtle()
