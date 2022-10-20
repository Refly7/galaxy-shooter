from turtle import Turtle
from time import sleep

pos = 0
xpos = -470
ypos = 450
size1 = 50
size2 = 20


class Messages(Turtle):

    def __init__(self):
        Turtle.__init__(self)

        self.penup      ()
        self.color      ('white')
        self.hideturtle ()


    def level(self, num):
        self.setposition(pos, pos)
        self.clear()
        self.write(f'Level {num}', False, 'center', ('Arial', size1, 'bold'))
        sleep(1)
        

    def refresh(self, hp):
        self.setposition(xpos, ypos)
        self.clear()
        self.write(f'{hp}', False, 'center', ('Arial', size2, 'bold'))


    def game_over(self):
        self.setposition(pos, pos)
        self.clear()
        self.write('Game Over', False, 'center', ('Arial', size1, 'bold'))
    

    def the_end(self, is_on):
        if is_on:
            self.setposition(pos, pos)
            self.clear()
            self.write('Victory!', False, 'center', ('Arial', size1, 'bold'))
