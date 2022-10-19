from math import degrees, atan
from random import choice
from missiles import Missiles
import turtle
import os

os.chdir("C:\\Users\\Lenovo\\Desktop\\Mój Folder\\Python\\100 dni\\galaxiga")
turtle.register_shape("monster.gif")

class Aliens():

    def __init__(self):
        self.allaliens = []


    def create_aliens_lvl_1(self):

        for j in range(4, 7, 2):                            # 2 rows
            for i in range(-4, 5, 2):                       # 5 aliens
                alien = turtle.Turtle("monster.gif")
                alien.penup()
                alien.setposition(i * 80, j * 60 + 300)
                alien.hp = 2
                alien.lvl = 1
                self.allaliens.append(alien)
        self.aliens = self.allaliens[::]



    def create_aliens_lvl_2(self):
        self.allaliens = []
        for i in range(-4, 5, 2):                       # 5 aliens
            alien = turtle.Turtle("monster.gif")
            alien.penup()
            alien.setposition(i * 80, 240 + 300)
            alien.hp = 1
            alien.lvl = 2
            self.allaliens.append(alien)
        self.aliens = self.allaliens[::]
        
        

    def create_aliens_lvl_3(self):
        self.allaliens = []
        

    def hit(self, alien):
        if alien.hp < 0:
            alien.hideturtle()
            self.aliens.pop(self.aliens.index(alien))


    def appearing(self):
        for alien in self.allaliens:
            alien.setheading(270)
            alien.forward(30)
            alien.homepos = alien.position()


    def move(self, alien):
        alien.forward(5 * alien.lvl)

        if abs(alien.distance(alien.homepos)) > 35 * alien.lvl:
            alien.setheading(alien.heading() + 45)


    def tracking(self, ship, alien):
        x = abs(ship.xcor() - alien.xcor())
        y = abs(ship.ycor() - alien.ycor())
        h = atan(y/x)

        if ship.xcor() > alien.xcor():
            return 360 - degrees(h)
        return 360 + degrees(h) + 180


    def shoot(self, ship):
        h = 270
        alien = choice(self.allaliens[:5] + [0] * 25)

        if alien == 0 or self.allaliens[self.allaliens.index(alien)] not in self.aliens:
            return

        if alien.lvl == 1 and self.allaliens[self.allaliens.index(alien) + 5] not in self.aliens:
            return

        elif alien.lvl == 1:
            alien = self.allaliens[self.allaliens.index(alien) + 5]

        if alien.lvl == 2:
            h = self.tracking(ship, alien)
        
        Missiles(alien.xcor(), alien.ycor() -20, h, 'LightSeaGreen')
