import math
import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.color('blue')
t.width(3)


screen = turtle.Screen()
screen.bgcolor("black")

# Center the graph horizontally and fit it to the screen
width = 2000
height = 400
screen.setworldcoordinates(-width//2, -height, width//2, height)

# Move turtle to starting position before drawing
start_x = -width // 2
start_y = 0
t.penup()
t.goto(start_x, start_y)
t.pendown()
t.color("#4646C8")


for i in range(1, width):
    changed_val = random.uniform(-1, 1) * 20  # Random variation
    wave = 100 * math.sin(i * 0.03  + math.sin(i * 0.01))
    x = i - width // 2
    y = wave
    if i == 1:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

turtle.done()
