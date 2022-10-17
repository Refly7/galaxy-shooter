from turtle import Screen
from ship import Ship
from stars import Stars
from lives import Lives
from aliens import Aliens
from missiles import allbullets

game_on = True
screen  = Screen()
screen.setup(1000, 1000)
screen.bgcolor('black')
screen.title('Galaxiga')
screen.tracer(0)

stars   = Stars()
lives   = Lives()
ship    = Ship()
aliens  = Aliens()          #aka ALCATOPUS
screen.update()

screen.listen()
screen.onkeypress(ship.up, key = 'Up')
screen.onkeypress(ship.down, key = 'Down')
screen.onkeypress(ship.left, key = 'Left')
screen.onkeypress(ship.right, key = 'Right')
screen.onkey(ship.shoots, key = 'space')


while game_on:

    screen.update()
    stars.move()
    aliens.shoot()
    
    for alien in aliens.aliens:
        aliens.move(alien)

        if ship.distance(alien) < 50:
            ship.hp -= 1
            lives.refresh(ship.hp)
            ship.home()
    
    for bullet in allbullets:
        bullet.move()

        for alien in aliens.aliens:
            bullet.collision(alien)
            aliens.hit(alien)

        if bullet.collision(ship):
            lives.refresh(ship.hp)

    if ship.hp < 0:
        lives.game_over()
        stars.stars = []
        break

    if len(aliens.aliens) == 0:
        screen.update()
        lives.the_end()
        stars.speed = 10
        break

for s in stars.stars:
    ship.setposition(0, -100)
    screen.update()
    stars.move()
    for bullet in allbullets:
        bullet.hideturtle()

screen.exitonclick()
