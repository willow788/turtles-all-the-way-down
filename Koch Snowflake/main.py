import turtle

def koch_curve(t, order, size, color_func=None, depth=0):
    """
    Draws a Koch curve of a given order and size using a turtle object.
    """
    # Accepts color_func and depth as optional arguments for compatibility
    import inspect
    args = inspect.getfullargspec(koch_curve).args
    color_func = None
    depth = 0
    if len(args) >= 4:
        try:
            color_func = locals()['color_func']
            depth = locals()['depth']
        except KeyError:
            pass
    if 'color_func' in locals() and color_func:
        t.pencolor(color_func(depth))
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3, color_func, depth + 1)
            t.left(angle)

def draw_snowflake(size, order):
    """
    Draws a complete Koch snowflake (three Koch curves joined as an
    equilateral triangle).
    """
    import colorsys

    def color_gradient(depth):
        # Create a blue-cyan-white gradient based on recursion depth
        hue = 0.55 + 0.15 * (depth / (order + 2))  # blue to cyan
        light = 0.5 + 0.5 * (depth / (order + 2))  # lighter at tips
        r, g, b = colorsys.hls_to_rgb(hue, light, 1.0)
        return (r, g, b)

    screen = turtle.Screen()
    screen.setup(700, 700)
    screen.bgcolor("#101020")
    screen.title("Beautiful Koch Snowflake")
    screen.tracer(0, 0)  # Turn off animation for instant drawing

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.width(3)
    t.penup()
    t.goto(-size / 2, size / 3.464)
    t.pendown()
    t.pensize(3)
    t.pencolor(color_gradient(0))
    t.fillcolor("#aaffff")

    # Draw a glowing effect by drawing the snowflake multiple times with increasing width and alpha
    for glow in range(8, 1, -2):
        t.penup()
        t.goto(-size / 2, size / 3.464)
        t.pendown()
        t.pensize(glow)
        t.pencolor((0.5, 1, 1))
        for _ in range(3):
            koch_curve(t, order, size, lambda d: (0.5, 1, 1), 0)
            t.right(120)

    # Main snowflake with gradient
    t.penup()
    t.goto(-size / 2, size / 3.464)
    t.pendown()
    t.pensize(3)
    for i in range(3):
        koch_curve(t, order, size, color_gradient, 0)
        t.right(120)

    # Fill the inside of the snowflake with small dots
    import random
    dot_color = color_gradient(order)
    # Estimate the bounding box for the snowflake (cover more area)
    min_x = -size / 2 * 1.05
    max_x = size / 2 * 1.05
    min_y = -size / 2 * 0.65
    max_y = size / 3**0.5 * 1.05
    # Use a separate turtle for dots
    dot_t = turtle.Turtle()
    dot_t.hideturtle()
    dot_t.penup()
    dot_t.speed(0)
    dot_t.pensize(1)
    dot_t.color(dot_color)
    num_dots = 2000
    v1 = (-size/2, -size/(2*3**0.5))
    v2 = (size/2, -size/(2*3**0.5))
    v3 = (0, size/3**0.5)
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    for _ in range(num_dots):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        pt = (x, y)
        b1 = sign(pt, v1, v2) < 0.0
        b2 = sign(pt, v2, v3) < 0.0
        b3 = sign(pt, v3, v1) < 0.0
        if (b1 == b2) and (b2 == b3):
            dot_t.goto(x, y)
            dot_t.dot(2)

    # Fill the 3 outer corners (outside the main triangle but inside the snowflake boundary)
    # These are the 3 equilateral triangles at each corner
    corner_dots = num_dots // 3
    # Corner 1 (left)
    cx1, cy1 = v1
    for _ in range(corner_dots):
        # Place dots in a triangle at the left corner
        rx = random.uniform(-size/2 - size/6, -size/2)
        ry = random.uniform(-size/(2*3**0.5), -size/(2*3**0.5) + size/3.464)
        # Check if inside the small triangle
        v1c = (-size/2, -size/(2*3**0.5))
        v2c = (-size/2 - size/6, -size/(2*3**0.5) + size/3.464)
        v3c = (-size/2 + size/6, -size/(2*3**0.5) + size/3.464)
        ptc = (rx, ry)
        b1c = sign(ptc, v1c, v2c) < 0.0
        b2c = sign(ptc, v2c, v3c) < 0.0
        b3c = sign(ptc, v3c, v1c) < 0.0
        if (b1c == b2c) and (b2c == b3c):
            dot_t.goto(rx, ry)
            dot_t.dot(2)
    # Corner 2 (right)
    for _ in range(corner_dots):
        rx = random.uniform(size/2, size/2 + size/6)
        ry = random.uniform(-size/(2*3**0.5), -size/(2*3**0.5) + size/3.464)
        v1c = (size/2, -size/(2*3**0.5))
        v2c = (size/2 + size/6, -size/(2*3**0.5) + size/3.464)
        v3c = (size/2 - size/6, -size/(2*3**0.5) + size/3.464)
        ptc = (rx, ry)
        b1c = sign(ptc, v1c, v2c) < 0.0
        b2c = sign(ptc, v2c, v3c) < 0.0
        b3c = sign(ptc, v3c, v1c) < 0.0
        if (b1c == b2c) and (b2c == b3c):
            dot_t.goto(rx, ry)
            dot_t.dot(2)
    # Corner 3 (top)
    for _ in range(corner_dots):
        rx = random.uniform(-size/12, size/12)
        ry = random.uniform(size/3**0.5, size/3**0.5 + size/3.464)
        v1c = (0, size/3**0.5)
        v2c = (-size/12, size/3**0.5 + size/3.464)
        v3c = (size/12, size/3**0.5 + size/3.464)
        ptc = (rx, ry)
        b1c = sign(ptc, v1c, v2c) < 0.0
        b2c = sign(ptc, v2c, v3c) < 0.0
        b3c = sign(ptc, v3c, v1c) < 0.0
        if (b1c == b2c) and (b2c == b3c):
            dot_t.goto(rx, ry)
            dot_t.dot(2)

    screen.update()
    t.hideturtle()
    dot_t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    snowflake_size = 420
    recursion_order = 4
    draw_snowflake(snowflake_size, recursion_order)
