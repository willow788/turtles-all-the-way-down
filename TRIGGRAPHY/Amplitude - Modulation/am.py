import turtle
import math

t = turtle.Turtle()
t.speed(0)
# t.hideturtle()  # Commented out to show the turtle while drawing
#innitialised turtle pen

screen = turtle.Screen()
screen.bgcolor("black")


t.color('yellow')
t.width(4)


# Center the graph horizontally and fit it to the screen
width = 2000
height = 200
screen.setworldcoordinates(-width//2, -height, width//2, height)


# Move turtle to starting position before drawing
carrier = math.sin(0 * 0.02)
modulating = math.sin(0 * 0.05)
modulated_wave = 150 * carrier * modulating
start_x = 0 - width // 2
start_y = modulated_wave
t.penup()
t.goto(start_x, start_y)
t.pendown()
t.color('yellow')

for i in range(1, width):
    carrier = math.sin(i * 0.02)
    modulating = math.sin(i * 0.05)
    modulated_wave = 100 * carrier * modulating
    x = i - width // 2
    y = modulated_wave
    t.goto(x, y)

turtle.done()
