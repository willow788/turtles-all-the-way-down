import turtle
import random
import math
import matplotlib.pyplot as plt

from matplotlib.pyplot import grid

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("black")

t.color("#45AA21")  
t.width(2)
t.penup()
t.goto(-300, 0)
t.pendown()
grid_size = 20


for i in range(-300, 300):
    y = (
        60 * math.sin(math.radians(i)) +
        30 * math.sin(math.radians(3 * i)) +
        15 * math.sin(math.radians(5 * i))

    )
   
  

    t.goto(i, y)

turtle.done()
