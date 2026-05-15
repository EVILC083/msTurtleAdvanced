import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("House on a Hill")

pen = turtle.Turtle()
pen.speed(3)
pen.hideturtle()

def draw_square(size, color):
    pen.setheading(0)
    pen.color(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

def draw_triangle(size, color):
    pen.setheading(0)
    pen.color(color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def draw_rectangle(width, height, color):
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

def draw_hill(center_x, center_y, radius, color):
    # Draw a large filled circle with center below the scene so only the top reads as a hill.
    pen.penup()
    pen.goto(center_x, center_y - radius)
    pen.setheading(0)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_cloud(x, y, scale=1.0):
    pen.color("white")
    for dx, dy, size in [
        (0, 0, 35),
        (25, 10, 40),
        (50, 0, 35),
        (20, -8, 30),
    ]:
        pen.penup()
        pen.goto(x + dx * scale, y + dy * scale)
        pen.dot(size * scale)

def draw_tree(x, y):
    # Trunk
    pen.penup()
    pen.goto(x, y)
    pen.setheading(90)
    pen.pendown()
    draw_rectangle(80, 24, "sienna")

    # Leaf canopy
    for dx, dy, size in [
        (-18, 82, 50),
        (6, 100, 60),
        (30, 84, 50),
        (6, 72, 45),
    ]:
        pen.penup()
        pen.goto(x + 12 + dx, y + dy)
        pen.dot(size, "forest green")

# Grassy hill
draw_hill(0, -300, 380, "#bf4b4b")

# House base
pen.penup()
pen.goto(-50, 0)
pen.pendown()
draw_square(100, "tan")

# Roof
pen.penup()
pen.goto(-50, 0)
pen.pendown()
draw_triangle(100, "red")

# Sun
pen.penup()
pen.goto(300, 300)
pen.pendown()
pen.color("orange")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# Clouds
draw_cloud(-190, 150, 1.0)
draw_cloud(-40, 180, 0.8)

# Tree
draw_tree(120, -20)

turtle.done()