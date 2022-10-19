from turtle import Screen
from ship import Ship
from stars import Stars
from messages import Messages
from aliens import Aliens
from missiles import allbullets


screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor('black')
screen.title('Galaxiga')
screen.tracer(0)

stars       = Stars()
messages    = Messages()
ship        = Ship()
aliens      = Aliens()          #aka ALCATOPUS
screen.update()


screen.listen()
screen.onkeypress(ship.up, key = 'Up')
screen.onkeypress(ship.down, key = 'Down')
screen.onkeypress(ship.left, key = 'Left')
screen.onkeypress(ship.right, key = 'Right')
screen.onkey(ship.shoots, key = 'space')


def fast_flying():
    stars.speed = 15
    for s in stars.stars:
        ship.setposition(0, -200)
        screen.update()
        stars.move()

        for bullet in allbullets:
            bullet.erase()
    stars.speed = 2


def enterence(create_aliens):
    fast_flying()
    create_aliens()

    for i in range(11):
        screen.update()
        aliens.appearing()


def aliens_move():
    for alien in aliens.aliens:
        aliens.move(alien)

        if ship.distance(alien) < 50:
            ship.hp -= 1
            messages.refresh(ship.hp)
            ship.home()


def bullets_move():
    for bullet in allbullets:
        bullet.move()

        for alien in aliens.aliens:
            bullet.collision(alien)
            aliens.hit(alien)

        if bullet.collision(ship):
            messages.refresh(ship.hp)


def win_lose():

    if ship.hp < 0:
        messages.game_over()
        stars.stars = []
        return False, False

    if len(aliens.aliens) == 0:
        return False, True

    return True, None


def level_active(is_on, lvl, alienslvl):
    level_on = is_on

    if level_on:
        enterence(alienslvl)
        messages.level(lvl)
        messages.refresh(ship.hp)

    while level_on:
        screen.update()
        stars.move()
        aliens.shoot(ship)
        aliens_move()
        bullets_move()
        level_on, is_on = win_lose()
    return is_on


# LEVEL 1
is_on = level_active(True, 1, aliens.create_aliens_lvl_1)
is_on = True

# LEVEL 2
is_on = level_active(is_on, 2, aliens.create_aliens_lvl_2)


# LEVEL 3
is_on = level_active(is_on, 3, aliens.create_aliens_lvl_3)

messages.the_end(is_on)
fast_flying()
screen.exitonclick()
