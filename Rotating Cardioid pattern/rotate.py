import turtle
import math
import random

#inniytialised turtle pen
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

#initializing the screen
screen = turtle.Screen()
screen.bgcolor("black")

t.color('cyan')

def draw_cardioid(scale, rotation, color):
    t.penup()
    first = True

    for i in range(0, 360):
        theta = math.radians(i)

        r = scale * (1 - math.sin(theta))

        x  = r * math.cos(theta + rotation)
        y  = r * math.sin(theta + rotation)

        xr = x + (random.randint(-10, 10))
        yr = y + (random.randint(-10, 10))

        if first:
            t.goto(xr, yr)
            t.pendown()
            first = False

        else:
            t.goto(xr, yr)


for i in range(12):
    draw_cardioid(scale= 120,
                  rotation= math.radians(i * 30),
                    color= (random.random(), random.random(), random.random()))
    
turtle.done()
