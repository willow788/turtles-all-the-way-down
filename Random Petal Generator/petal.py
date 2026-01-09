#random petal color generator
# This script generates a random color for a petal using RGB values.

import random
import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
#innitialised turtle pen

#initializing the screen
screen = turtle.Screen()
screen.bgcolor("black")

t.color('green')
t.width(2)

petal = random.randint(5, 12)
base_radius = 150
angle = 360 / petal
noise_strength = 30

t.penup()
first= True

for i in range(0, 2000):
    theta = i * 0.01
    noise = random.randint(-noise_strength, noise_strength)

    r = base_radius * math.sin(petal * theta) + noise

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    if first:
        t.goto(x,y)
        t.pendown()
        first = False
        t.hideturtle()
    else:
        t.goto(x,y)

t.penup()
turtle.done()
