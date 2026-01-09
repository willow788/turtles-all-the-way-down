import turtle
import random
import math

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

#screen initialization
screen = turtle.Screen()
screen.bgcolor("black")

t.penup()
t.goto(-300, 0)
t.pendown()
t.color("hotpink")

for i in range(-300, 300):
    y = 80 * math.sin(math.radians(i))
    t.goto(i, y)

turtle.done()
