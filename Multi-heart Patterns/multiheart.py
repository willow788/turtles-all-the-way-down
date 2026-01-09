import numpy as np
import turtle 
import math
import random

#init turtle pen
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")
t.width(2)
import colorsys

def draw_multiple_Hearts(scale, angle, color):
    t.color(color)
    t.penup()

    first = True
    for i in range(0, 360):
        rad = math.radians(i)

        x = scale * 16 * math.sin(rad) ** 3
        y = scale * (13 * math.cos(rad) 
                    - 5 * math.cos(2 * rad) 
                    - 2 * math.cos(3 * rad) 
                    - math.cos(4 * rad)
                    )
        
        #rotation
        x_rotation = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
        y_rotation = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle))

        if first:
            t.goto(x_rotation, y_rotation)
            t.pendown()
            first = False
        else:
            t.goto(x_rotation, y_rotation)
    t.penup()


colors = ['red', 'pink', 'magenta', 'orange', 'yellow', 'purple']

for i in range(36):
    draw_multiple_Hearts(scale=10,
                         angle= i * 10,
                         color=random.choice(colors))
    

turtle.done()

