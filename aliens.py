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
                alien.hp = 2                        # type: ignore
                self.allaliens.append(alien)
        self.aliens = self.allaliens[::]



    def create_aliens_lvl_2(self):
        self.allaliens = []
        
        

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
        alien.forward(5)

        if abs(alien.distance(alien.homepos)) > 35:
            alien.setheading(alien.heading() + 45)


    def shoot(self):
        
        alien = choice(self.allaliens[:5] + [0] * 25)

        if alien == 0 or self.allaliens[self.allaliens.index(alien) + 5] not in self.aliens:
            return

        if alien not in self.aliens:
            alien = self.allaliens[self.allaliens.index(alien) + 5]

        Missiles(alien.xcor(), alien.ycor() - 15, -1, 'LightSeaGreen')
