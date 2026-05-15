def draw():
    # This function draws things on the screen
    pass


def update():
    # This function updates the game over and over
    pass
WIDTH = 800
HEIGHT = 500
def draw():
    screen.clear()
    player = Rect((100, 400), (40, 40))
    def draw():
    screen.clear()
    screen.draw.filled_rect(player, "blue")
    player = Rect((100, 400), (40, 40))
    def update():
    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5
        player.x += 5
def update():
    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH
        velocity_y = 0
gravity = 1
def update():
    global velocity_y

    velocity_y += gravity
    player.y += velocity_y
    def update():
    global velocity_y

    velocity_y += gravity
    player.y += velocity_y

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        gravity = 0.5
        gravity = 2
        on_ground = False
        velocity_y = -15
platforms = [
    Rect((0, 470), (800, 30)),
    Rect((200, 380), (150, 20)),
    Rect((450, 300), (150, 20)),
    Rect((650, 220), (100, 20))
]def draw():
    screen.clear()
    screen.draw.filled_rect(player, "blue")

    for platform in platforms:
        screen.draw.filled_rect(platform, "green")
        Rect((100, 250), (120, 20))
        on_ground = False

for platform in platforms:
    if player.colliderect(platform) and velocity_y > 0:
        player.bottom = platform.top
        velocity_y = 0
        on_ground = True
        global velocity_y, on_ground
        player.colliderect(platform)
        velocity_y > 0
        coins = [
    Rect((250, 340), (20, 20)),
    Rect((500, 260), (20, 20)),
    Rect((690, 180), (20, 20))
]

score = 0
for coin in coins:
    screen.draw.filled_rect(coin, "yellow")
    global score

for coin in coins[:]:
    if player.colliderect(coin):
        coins.remove(coin)
        score += 1
        lava = Rect((350, 450), (100, 20))
        screen.draw.filled_rect(lava, "red")
        if player.colliderect(lava):
         player.x = 100
    player.y = 400
    velocity_y = 0
    goal = Rect((730, 420), (40, 50))
game_won = False
screen.draw.filled_rect(goal, "purple")
global  game_won

if player.colliderect(goal):
    game_won = True
    if game_won:
        screen.draw.text("You Win!", center=(400, 250), fontsize=60, color="yellow")
# Window settings
WIDTH = 800
HEIGHT = 500

# Player variables
player = Rect((100, 400), (40, 40))
velocity_y = 0
gravity = 1
on_ground = False

# Platforms
platforms = [
    Rect((0, 470), (800, 30)),
    Rect((200, 380), (150, 20))
]

# Collectibles
coins = []
score = 0

# Hazards and goal
lava = Rect((350, 450), (100, 20))
goal = Rect((730, 420), (40, 50))
game_won = False
def reset_player():
    player.x = 100
    player.y = 400
    reset_player()
    global score