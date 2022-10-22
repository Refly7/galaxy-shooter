from turtle import Screen
from ship import Ship
from stars import Stars
from messages import Messages
from aliens import Aliens
from missiles import allbullets
import keyboard

screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor('black')
screen.title('Galaxiga')
screen.tracer(0)

cooldown = 5
sspeed1 = 15
sspeed2 = 2
posx = 0
posy = -200
enemy_appearing_time = 11
ship_enemy_collision_distance = 50
dmg = 1

stars       = Stars()
messages    = Messages()
ship        = Ship()
aliens      = Aliens()          #aka ALCATOPUS
screen.update()

    
def inputs():
    
    if keyboard.is_pressed('esc'):
        print('ESC KEY pressed - quiting game now..')
        return False

    if keyboard.is_pressed('up'):
        ship.up()
    if keyboard.is_pressed('down'):
        ship.down()
    if keyboard.is_pressed('left'):
        ship.left()
    if keyboard.is_pressed('right'):
        ship.right()
    if keyboard.is_pressed('space') and not ship.cooldown:
        ship.shoots()
        ship.cooldown = cooldown

def fast_flying():
    stars.speed = sspeed1
    for s in stars.stars:
        ship.setposition(posx, posy)
        screen.update() 
        stars.move()

        for bullet in allbullets:
            bullet.erase()
    stars.speed = sspeed2


def enterence(create_aliens):
    fast_flying()
    create_aliens()

    for i in range(enemy_appearing_time):
        screen.update()
        aliens.appearing()


def aliens_move():
    for alien in aliens.aliens:
        aliens.move(alien)

        if not alien.isvisible():
            alien.showturtle()

        if ship.distance(alien) < ship_enemy_collision_distance:
            ship.hp -= dmg
            messages.refresh(ship.hp)
            ship.home()
        

def bullets_move():
    if not ship.isvisible():
        ship.showturtle()

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
        inputs()
        stars.move()
        aliens.shoot(ship)
        aliens_move()
        bullets_move()
        level_on, is_on = win_lose()

        if ship.cooldown > 0:
            ship.cooldown -= 1
    return is_on


# LEVEL 1
is_on = level_active(True, 1, aliens.create_aliens_lvl_1)

# LEVEL 2
is_on = level_active(is_on, 2, aliens.create_aliens_lvl_2)

# LEVEL 3
is_on = level_active(is_on, 3, aliens.create_aliens_lvl_3)

messages.the_end(is_on)
fast_flying()
screen.exitonclick()
