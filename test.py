from turtle import Turtle, Screen
import os

screen = Screen()
screen.screensize(800, 800)
os.chdir("C:\\Users\\Lenovo\\Desktop\\Mój Folder\\Python\\100 dni\\galaxiga")
screen.register_shape("ship.gif")

turtle = Turtle("ship.gif")
turtle.penup()  
turtle.goto(-280, -280)

screen.mainloop()