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

#screen setup
screen = turtle.Screen()
screen.bgcolor('black')
screen.title("plotting a nephroid curve")

#parameters
R = 150
r = R / 2
steps = 1000
hue_start = random.random()

# Center the drawing
centre_x = 0
centre_y = 0


# Calculate nephroid points once
points = []
for i in range(steps + 1):
    theta = 2 * math.pi * (i / steps)
    x = 3 * r * math.cos(theta) - r * math.cos(3 * theta)
    y = 3 * r * math.sin(theta) - r * math.sin(3 * theta)
    h = (theta / (2 * math.pi) + hue_start) % 1.0
    r_col, g_col, b_col = colorsys.hsv_to_rgb(h, 0.9, 1.0)
    points.append((x, y, r_col, g_col, b_col))

# Draw nephroid with different layers
def draw_nephroid(thickness=1, color=(1.0, 0.5, 0.5)):
    t.width(thickness)
    t.pencolor(*color)
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    for x, y, _, _, _ in points[1:]:
        t.goto(x, y)

#glow layers:


# Glow layers: pink/red shades
layers = [
    ((1.0, 0.5, 0.8), 8),  # light pink
    ((1.0, 0.3, 0.6), 5),  # medium pink
    ((1.0, 0.1, 0.3), 3),  # dark pink
]
for color, thickness in layers:
    draw_nephroid(thickness, color)

# Main curve with rainbow gradient
t.width(2)
t.penup()
t.goto(points[0][0], points[0][1])
t.pendown()
for x, y, r_col, g_col, b_col in points:
    t.pencolor(r_col, g_col, b_col)
    t.goto(x, y)

turtle.done()
