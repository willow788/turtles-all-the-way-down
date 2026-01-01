from turtle import *
import math
import cmath
import turtle

t = turtle.Turtle()
# Create a turtle object

t.speed(0)  
# Set the fastest drawing speed

turtle.bgcolor("black") 
# Set background color to black

t.pensize(2) 
# Set pen size

colors= ["#BA0505", "#A06903", "#CECE1D", "#0DB686", "#101076", "#41aa0d", "#D51DAD"]  
# Define a list of colors

# Draw a colorful spiral
for i in range(200):
    t.color(colors[i % 7])   # Cycle through the colors
    t.circle(i)              #draw the circle with radius i
    t.left(59)               # Turn left by 59 degrees

turtle.done() # Finish the drawing
