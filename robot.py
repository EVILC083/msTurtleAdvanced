import turtle


screen = turtle.Screen()
screen.setup(width=1100, height=850)
screen.bgcolor("#101820")
screen.title("Advanced Turtle Robot")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()


def move_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def draw_rect(x, y, width, height, outline, fill):
    move_to(x, y)
    pen.setheading(0)
    pen.color(outline, fill)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()


def draw_rounded_rect(x, y, width, height, radius, outline, fill):
    move_to(x, y)
    pen.setheading(0)
    pen.color(outline, fill)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width - 2 * radius)
        pen.circle(-radius, 90)
        pen.forward(height - 2 * radius)
        pen.circle(-radius, 90)
    pen.end_fill()


def draw_panel_lines(x, y, width, height, rows, cols, color):
    pen.color(color)
    for r in range(1, rows):
        move_to(x, y - (height / rows) * r)
        pen.setheading(0)
        pen.forward(width)

    for c in range(1, cols):
        move_to(x + (width / cols) * c, y)
        pen.setheading(-90)
        pen.forward(height)


def draw_bolt(x, y, size, color):
    move_to(x, y)
    pen.dot(size, color)
    move_to(x, y - size / 5)
    pen.setheading(0)
    pen.color("#2b2b2b")
    pen.forward(size / 2)


def draw_head():
    draw_rounded_rect(-140, 210, 280, 170, 22, "#d8dee9", "#324a5f")
    draw_rect(-115, 172, 230, 55, "#d8dee9", "#24384a")
    draw_panel_lines(-115, 172, 230, 55, 3, 8, "#dfe8f7")

    for x in (-70, 70):
        move_to(x, 250)
        pen.dot(64, "#e6eef8")
        pen.dot(36, "#53d8fb")
        pen.dot(16, "#0b1f33")
        move_to(x - 12, 262)
        pen.dot(8, "#f5fdff")

    draw_rect(-70, 140, 140, 24, "#d8dee9", "#24384a")
    pen.color("#90a3b8")
    for i in range(9):
        move_to(-62 + i * 16, 140)
        pen.setheading(-90)
        pen.forward(24)

    for x in (-95, 95):
        move_to(x, 295)
        pen.color("#d8dee9")
        pen.setheading(90)
        pen.forward(42)
        pen.dot(18, "#f6c945")


def draw_torso():
    draw_rounded_rect(-190, 120, 380, 280, 26, "#d8dee9", "#3d5a73")
    draw_rect(-145, 65, 290, 95, "#d8dee9", "#26394b")
    draw_panel_lines(-145, 65, 290, 95, 4, 5, "#6f86a1")

    draw_rounded_rect(-95, 35, 190, 95, 14, "#b6c6d8", "#132530")
    for i in range(8):
        height = 22 + (i % 4) * 10
        x = -80 + i * 22
        draw_rect(x, 27, 12, height, "#75f0a7", "#3bd17d")

    move_to(0, 80)
    pen.dot(95, "#223342")
    pen.dot(66, "#58f1ff")
    pen.dot(22, "#d5f8ff")

    for x in (-165, -120, -75, 75, 120, 165):
        draw_bolt(x, 115, 12, "#cbd6e2")
        draw_bolt(x, -130, 12, "#cbd6e2")


def draw_arm(left=True):
    direction = -1 if left else 1
    shoulder_x = direction * 190

    draw_rounded_rect(
        shoulder_x + direction * 8,
        85,
        90,
        44,
        10,
        "#d8dee9",
        "#486987",
    )

    x = shoulder_x + direction * 28
    for _ in range(3):
        draw_rect(
            x,
            70,
            direction * 40 if left else 40,
            22,
            "#cdd8e6",
            "#324b62",
        )
        x += direction * 44

    move_to(direction * 355, 52)
    pen.dot(54, "#d8dee9")
    pen.dot(34, "#355066")

    arm_start = direction * 322
    draw_rounded_rect(
        arm_start,
        20,
        direction * 115 if left else 115,
        42,
        10,
        "#d8dee9",
        "#567a9b",
    )

    claw_x = direction * 440
    for i in range(3):
        offset = 22 - i * 14
        move_to(claw_x, 28 + offset)
        pen.setheading(0 if left else 180)
        pen.color("#d8dee9", "#8ea5bc")
        pen.begin_fill()
        pen.forward(30)
        pen.right(120)
        pen.forward(18)
        pen.right(120)
        pen.forward(18)
        pen.end_fill()


def draw_leg(left=True):
    x = -95 if left else 30
    draw_rounded_rect(x, -160, 65, 145, 12, "#d8dee9", "#4a6b89")

    move_to(x + 32, -20)
    pen.dot(54, "#ced9e6")
    pen.dot(34, "#2e4355")

    draw_rounded_rect(x - 8, -270, 80, 112, 12, "#d8dee9", "#3a566f")
    for i in range(4):
        draw_rect(x + 6 + i * 17, -208, 8, 42, "#7ed2f8", "#40bbea")

    draw_rounded_rect(x - 22, -285, 125, 42, 12, "#d8dee9", "#2f475d")
    for i in range(4):
        draw_bolt(x - 6 + i * 30, -250, 10, "#cbd6e2")


def draw_cable(left=True):
    direction = -1 if left else 1
    move_to(direction * 75, -140)
    pen.setheading(-90)
    pen.color("#8db0ca")
    for _ in range(10):
        pen.circle(direction * 9, 36)
        pen.circle(direction * -9, 36)


def draw_background():
    pen.color("#173346")
    for y in range(-350, -20, 30):
        move_to(-540, y)
        pen.setheading(0)
        pen.forward(1080)

    pen.color("#1e4a63")
    for x in range(-520, 540, 40):
        move_to(x, -350)
        pen.setheading(75)
        pen.forward(520)

    for x, y, c in [
        (-420, 310, "#59f8ff"),
        (-350, 260, "#96ffb7"),
        (-260, 330, "#f6c945"),
        (300, 300, "#59f8ff"),
        (430, 250, "#96ffb7"),
        (350, 340, "#f6c945"),
    ]:
        move_to(x, y)
        pen.dot(22, c)
        pen.dot(8, "#f8feff")


draw_background()
draw_head()
draw_torso()
draw_arm(left=True)
draw_arm(left=False)
draw_leg(left=True)
draw_leg(left=False)
draw_cable(left=True)
draw_cable(left=False)

turtle.donee()