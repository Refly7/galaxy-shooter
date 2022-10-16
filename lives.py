from turtle import Turtle

class Lives(Turtle):

    def __init__(self):
        Turtle.__init__(self)

        self.setposition(-470, 450)
        self.penup      ()
        self.color      ('white')
        self.hideturtle ()
        self.refresh    (3)
        

    def refresh(self, hp):
        self.clear()
        self.write(f'{hp}', False, 'center', ('Arial', 20, 'bold'))


    def game_over(self):
        self.setposition(0, 0)
        self.clear()
        self.write('Game Over', False, 'center', ('Arial', 50, 'bold'))
    

    def the_end(self):
        self.setposition(0, 0)
        self.clear()
        self.write('Victory!', False, 'center', ('Arial', 50, 'bold'))