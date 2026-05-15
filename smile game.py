WIDTH = 800
HEIGHT = 500

TITLE = "My Platformer Game"

player = Rect((100, 400), (40, 40))

velocity_y = 0
gravity = 1
jump_strength = -15
speed = 5

on_ground = False
score = 0
game_won = False
game_over = False
def draw():
    screen.clear()
    screen.fill("skyblue")
    screen.draw.filled_rect(player, "blue")
screen.draw.filled_rect(player, "red")
screen.draw.filled_rect(player, "purple")
screen.draw.filled_rect(player, "orange")
def update():
    global velocity_y

    if keyboard.left:
        player.x -= speed

    if keyboard.right:
        player.x += speed
        if player.left < 0:
    player.left = 0

if player.right > WIDTH:
    player.right = WIDTH
    velocity_y += gravity
player.y += velocity_y
platforms = [
    Rect((0, 470), (800, 30)),
    Rect((150, 390), (120, 20)),
    Rect((350, 320), (120, 20)),
    Rect((550, 250), (120, 20)),
    Rect((250, 180), (120, 20))
]for platform in platforms:
    screen.draw.filled_rect(platform, "green")
    Examples:

screen.draw.filled_rect(platform, "brown")   # wood
screen.draw.filled_rect(platform, "gray")    # stone
screen.draw.filled_rect(platform, "white")   # clouds
screen.draw.filled_rect(platform, "darkgreen") # jungle