import turtle
import math
import random
from turtle import *
import colorsys




# Initialize turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(3)
turtle.colormode(1.0)  # Use 0-1 range for RGB



# Screen setup
screen = turtle.Screen()
screen.bgcolor("#151414")
screen.title("Circsine Curve - Pretty Version")


freq = 5
t.penup()

# Parameters
base_Radious = 150
amplitude = 20
freq = 5
steps = 1000
hue_start = random.random()

# Center the drawing
t.penup()
t.goto(0, 0)
t.pendown()

# Glow effect: draw blurred shadow
for glow in range(10, 0, -2):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.width(glow)
    t.pencolor(0.4, 0.4, 0.4)  # light gray for glow
    for i in range(steps + 1):
        theta = 2 * math.pi * freq * (i / steps)
        radi = base_Radious + amplitude * math.sin(freq * theta)
        x = radi * math.cos(theta)
        y = radi * math.sin(theta)
        if i == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

# Main curve with color gradient
t.width(3)
t.penup()
t.goto(0, 0)
t.pendown()
for i in range(steps + 1):
    theta = 2 * math.pi * freq * (i / steps)
    radi = base_Radious + amplitude * math.sin(freq * theta)
    x = radi * math.cos(theta)
    y = radi * math.sin(theta)
    hue = (hue_start + i / steps) % 1.0
    r_col, g_col, b_col = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
    t.pencolor(r_col, g_col, b_col)
    if i == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

# Add a title in the center
t.penup()
t.goto(0, -base_Radious - 40)
t.pencolor("white")
t.write("Circsine Curve", align="center", font=("Arial", 20, "bold"))

turtle.done()
