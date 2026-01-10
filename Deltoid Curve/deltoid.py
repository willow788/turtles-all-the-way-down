import turtle
import math
import random
from turtle import *
import colorsys


# Init turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)
turtle.colormode(1.0)  


# Screen setup
screen = turtle.Screen()
screen.bgcolor('black')
screen.title("Deltoid Curve - Pretty Version")

#initialising the parameters
R = 150
r = R / 3
steps = 1000
hue_start = random.random()


# Center the drawing
center_x = 0
center_y = 0


r
points = []
for i in range(steps + 1):
    theta = 2 * math.pi * (i / steps)
    x = 2 * r * math.cos(theta) + r * math.cos(2 * theta)
    y = 2 * r * math.sin(theta) - r * math.sin(2 * theta)
    points.append((x, y))

for glow, pink in zip([6, 4, 2], [0.9, 0.7, 0.5]):
    t.width(glow)
    # Pink color (R high, G low, B high)
    t.pencolor(pink, 0.2, pink)
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    for x, y in points[1:]:
        t.goto(x, y)

t.width(2)
t.penup()
t.goto(points[0][0], points[0][1])
t.pendown()
for i, (x, y) in enumerate(points):
    hue = (hue_start + i / steps) % 1.0
    r_col, g_col, b_col = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
    t.pencolor(r_col, g_col, b_col)
    t.goto(x, y)

t.penup()
t.goto(0, -R - 40)
t.pencolor("white")
t.write("Deltoid Curve", align="center", font=("Arial", 20, "bold"))

turtle.done()

