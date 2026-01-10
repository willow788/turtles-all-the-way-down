import turtle
import math
import random
import colorsys
from turtle import *

screen = turtle.Screen()
screen.bgcolor("#151414")


t = turtle.Turtle()
t.speed('fastest')
t.hideturtle()
t.width(1)

base_rad = 150
A = 20
B = 30
freq = 5
n = 7

m = 14
phi = math.pi / 4
steps = 6000


def draw_Star(scale, thickness, hue_shift):
    t.penup()
    t.pensize(1)  # Always use fine lines

    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
        r = base_rad + A * math.sin(freq * theta) + B * math.sin(n * theta + phi)
        r *= scale

        x = r * math.cos(theta)
        y = r * math.sin(theta)

        h = (theta / (2 * math.pi) + hue_shift) % 1.0
        r_col, g_col, b_col = colorsys.hsv_to_rgb(h, 0.9, 1.0)
        t.pencolor(r_col, g_col, b_col)

        if i == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

# Draw glow layers with fine lines
layers = [
    (1.2, 1, 0.6),  # outer glow, fine line
    (1.1, 1, 0.8),  # middle glow, fine line
    (1.05, 1, 1.0)  # inner glow, fine line
]
for layer in layers:
    scale, thickness, hue_shift = layer
    draw_Star(scale, thickness, hue_shift)
turtle.done()
