from turtle import *
import math
import cmath
import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pensize(2)
colors= ["#BA0505", "#A06903", "#CECE1D", "#0DB686", "#101076", "#41aa0d", "#D51DAD"]

for i in range(200):
    t.color(colors[i % 7])
    t.circle(i)
    t.left(59)

turtle.done()
