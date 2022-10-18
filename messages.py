from turtle import Turtle
from time import sleep

class Messages(Turtle):

    def __init__(self):
        Turtle.__init__(self)

        self.penup      ()
        self.color      ('white')
        self.hideturtle ()


    def level(self, num):
        self.setposition(0, 0)
        self.clear()
        self.write(f'Level {num}', False, 'center', ('Arial', 50, 'bold'))
        sleep(1)
        

    def refresh(self, hp):
        self.setposition(-470, 450)
        self.clear()
        self.write(f'{hp}', False, 'center', ('Arial', 20, 'bold'))


    def game_over(self):
        self.setposition(0, 0)
        self.clear()
        self.write('Game Over', False, 'center', ('Arial', 50, 'bold'))
    

    def the_end(self, is_on):
        if is_on:
            self.setposition(0, 0)
            self.clear()
            self.write('Victory!', False, 'center', ('Arial', 50, 'bold'))