import turtle
import random
import math

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
#innitialised turtle pen

#initializing the screen
screen = turtle.Screen()
screen.bgcolor("black")
t.color('gold')

radious = 150
lines = 120
line_length = 300

for i in range(lines):
    angles  = 2 * math.pi / lines

    x = radious * math.cos(angles * i)
    y = radious * math.sin(angles * i)

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(math.degrees(angles * i))
    t.forward(line_length)

turtle.done()

