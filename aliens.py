from math import degrees, atan
from random import choice
from missiles import Missiles
import turtle

distance = 20
distance_boss = 80
posx1 = 80
posx2 = 0
posy1 = 60
posy2 = 300
hp1 = 2
hp2 = 9
h = 270
speed = 30
turn = 45
distance_from_home = 35
atk_frequency = 25          # the greater the number the smaller the frequency
bullet_speed1 = 10
bullet_speed2 = 20

turtle.register_shape("monster.gif")
turtle.register_shape("boss.gif")


class Aliens():

    def __init__(self):
        self.allaliens = []


    def create_aliens_lvl_1(self):

        for j in range(4, 7, 2):                            # 2 rows
            for i in range(-4, 5, 2):                       # 5 aliens
                alien = turtle.Turtle("monster.gif")
                alien.penup()
                alien.setposition(i * posx1, j * posy1 + posy2)
                alien.hp = hp1
                alien.lvl = 1
                self.allaliens.append(alien)
        self.aliens = self.allaliens[::]


    def create_aliens_lvl_2(self):
        self.allaliens = []
        for i in range(-4, 5, 2):                       # 5 aliens
            alien = turtle.Turtle("monster.gif")
            alien.penup()
            alien.setposition(i * posx1, 4 * posy1 + posy2)
            alien.hp = hp1
            alien.lvl = 2
            self.allaliens.append(alien)
        self.aliens = self.allaliens[::]     
       

    def create_aliens_lvl_3(self):
        self.allaliens = []
        alien = turtle.Turtle("boss.gif")
        alien.penup()
        alien.setposition(posx2, 4 * posy1 + posy2)
        alien.hp = hp2
        alien.lvl = 3
        self.allaliens.append(alien)

        for i in range(-4, 5, 8):                       # 2 aliens
            alien = turtle.Turtle("monster.gif")
            alien.penup()
            alien.setposition(i * posx1, 4 * posy1 + posy2)
            alien.hp = hp1
            alien.lvl = 2
            self.allaliens.append(alien)
        self.aliens = self.allaliens[::]
        

    def hit(self, alien):
        if alien.hp < 0:
            alien.hideturtle()
            self.aliens.pop(self.aliens.index(alien))


    def appearing(self):
        for alien in self.allaliens:
            alien.setheading(h)
            alien.forward(speed)
            alien.homepos = alien.position()


    def move(self, alien):
        alien.forward(4 * alien.lvl)

        if abs(alien.distance(alien.homepos)) > distance_from_home * alien.lvl:
            alien.setheading(alien.heading() + turn)


    def tracking(self, ship, alien):
        x = abs(ship.xcor() - alien.xcor())
        y = abs(ship.ycor() - alien.ycor())

        if x == 0:
            x = 1 * 10 ** -14

        h = atan(y/x)

        if ship.xcor() > alien.xcor():
            return 360 - degrees(h)
        return 360 + degrees(h) + 180


    def shoot(self, ship):
        alien = choice(self.allaliens[:5] + [0] * atk_frequency)

        if alien == 0:
            return
        
        if  self.allaliens[self.allaliens.index(alien)] not in self.aliens:
            if alien.lvl == 1 and self.allaliens[self.allaliens.index(alien) + 5] in self.aliens:
                alien = self.allaliens[self.allaliens.index(alien) + 5]
                Missiles(alien.xcor(), alien.ycor() - distance, 'LightSeaGreen', h) 
            return

        if self.aliens[0].lvl == 3 and self.aliens[0] != alien and choice([1, 0]):
            for i in range(-15, 15, 5):
                Missiles(self.allaliens[0].xcor(), self.allaliens[0].ycor() - distance_boss, 'LightSeaGreen', h + i * 3, bullet_speed1)

        if alien.lvl >= 2:
            h = self.tracking(ship, alien)
        
        if alien.lvl == 3:
            for i in range(-3, 3):
                Missiles(alien.xcor() + i * 15, alien.ycor() - distance_boss, 'LightSeaGreen', h, bullet_speed2)

        Missiles(alien.xcor(), alien.ycor() - distance, 'LightSeaGreen', h) 
