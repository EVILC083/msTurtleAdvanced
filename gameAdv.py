"""
Basic Platformer Game Example
Demonstrates: Player, Platforms, Coins, Enemy, Goal, Score, Win/Lose conditions
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LEVEL_WIDTH = 2400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RGB = (0, 128, 255)
# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrolling Platformer Game")
clock = pygame.time.Clock()

# ===== PLAYER =====
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/archer.gif')
        self.image = pygame.transform.scale(self.image, (33, 44))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.vel_y = 0
        self.vel_x = 0
        self.is_jumping = False
        self.gravity = 0.6
        self.jump_power = -15
        self.speed = 5
        self.level_width = LEVEL_WIDTH
    
    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
        else:
            self.vel_x = 0
        
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.vel_y = self.jump_power
            self.is_jumping = True
    
    def apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        
        # Check if player fell off screen
        if self.rect.y > SCREEN_HEIGHT:
            return False
        return True
    
    def update(self, platforms):
        self.rect.x += self.vel_x
        
        # Keep player inside the world boundaries
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > self.level_width - self.rect.width:
            self.rect.x = self.level_width - self.rect.width
        
        # Check collision with platforms
        for platform in platforms:
            if self.vel_y > 0 and self.rect.bottom >= platform.rect.top and self.rect.top < platform.rect.top:
                if self.rect.right > platform.rect.left and self.rect.left < platform.rect.right:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.is_jumping = False
    
    def draw(self, surface, camera_x):
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y))


# ===== PLATFORM =====
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, surface, camera_x):
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Create a small red rectangle as the bullet
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        # Set starting position to the player's location
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10  # Moves upward

# ===== COIN (Collectible) =====
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collected = False
    
    def draw(self, surface, camera_x):
        if not self.collected:
            surface.blit(self.image, (self.rect.x - camera_x, self.rect.y))


# ===== ENEMY =====
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/monster.gif')
        self.image = pygame.transform.scale(self.image, (33, 44))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 2
        self.direction = 1
        self.left_bound = x - 80
        self.right_bound = x + 80
    
    def update(self):
        self.rect.x += self.speed * self.direction
        
        # Change direction at bounds
        if self.rect.x <= self.left_bound or self.rect.x >= self.right_bound:
            self.direction *= -1
    
    def draw(self, surface, camera_x):
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y))


# ===== GOAL/FINISH AREA =====
class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, surface, camera_x):
        surface.blit(self.image, (self.rect.x - camera_x, self.rect.y))


# ===== GAME =====
class Game:
    def __init__(self):
        self.player = Player(50, 400)
        self.camera_x = 0
        
        # Create platforms
        self.platforms = [
            Platform(0, SCREEN_HEIGHT - 40, LEVEL_WIDTH, 40),  # Ground
            Platform(200, 450, 150, 20),
            Platform(500, 400, 150, 20),
            Platform(100, 300, 150, 20),
            Platform(600, 300, 150, 20),
            Platform(900, 500, 140, 20),
            Platform(1150, 420, 150, 20),
            Platform(1400, 350, 150, 20),
            Platform(1700, 460, 140, 20),
            Platform(1950, 320, 180, 20),
        ]
        
        # Create coin
        self.coin = Coin(1200, 370)
        
        # Create enemy
        self.enemy = Enemy(1550, 430)
        self.enemy2 = Enemy(2000, 430)
        self.enemy3 = Enemy(300, 430)
        
        # Create goal
        self.goal = Goal(2200, 260)
        
        self.score = 0
        self.game_over = False
        self.won = False
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def update(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        
        if not self.player.apply_gravity():
            self.game_over = True
        
        self.player.update(self.platforms)
        self.enemy.update()
        self.enemy2.update()
        self.enemy3.update()

        self.rect.y += self.speedy
        # Kill the bullet if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
    

        # Check coin collision
        if (not self.coin.collected and 
            self.player.rect.colliderect(self.coin.rect)):
            self.coin.collected = True
            self.score += 10
        
        # Check enemy collision (lose condition)
        if self.player.rect.colliderect(self.enemy.rect):
            self.game_over = True
        
        if self.player.rect.colliderect(self.enemy2.rect):
            self.game_over = True
        
        # Check goal collision (win condition)
        if self.player.rect.colliderect(self.goal.rect):
            self.won = True

        # Move camera to follow the player, centered when possible.
        target_camera_x = self.player.rect.centerx - SCREEN_WIDTH // 2
        self.camera_x = max(0, min(target_camera_x, LEVEL_WIDTH - SCREEN_WIDTH))
    
    def draw(self):
        screen.fill("Grey")
        
        # Draw game elements
        for platform in self.platforms:
            platform.draw(screen, self.camera_x)
        
        self.coin.draw(screen, self.camera_x)
        self.enemy.draw(screen, self.camera_x)
        self.enemy2.draw(screen, self.camera_x)

        self.goal.draw(screen, self.camera_x)
        self.player.draw(screen, self.camera_x)
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        # Draw game state
        if self.game_over:
            game_over_text = font.render("GAME OVER - Press R to Restart", True, RED)
            screen.blit(game_over_text, (200, 250))
        
        if self.won:
            win_text = font.render("YOU WIN! - Press R to Restart", True, GREEN)
            screen.blit(win_text, (200, 250))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            
            if not self.game_over and not self.won:
                self.update()
            
            # Check for restart
            keys = pygame.key.get_pressed()
            if (self.game_over or self.won) and keys[pygame.K_r]:
                self.__init__()
            
            self.draw()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()


# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
    import pygame
import sys

# Initialize Pygame
pygame.init()

# Setup Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# --- Enemy Class ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Use a red rectangle placeholder if you don't have an image file yet
        self.image = pygame.image.load('images/monster.gif')
        self.image = pygame.transform.scale(self.image, (33, 44))
        
        # Get position boundaries
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 4

    def update(self):
        # Move horizontal
        self.rect.x += self.speed
        
        # Bounce off walls
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed *= -1

# --- Game Setup ---
enemy_group = pygame.sprite.Group()

# Spawn 3 enemies at different heights
enemy1 = Enemy(100, 100)
enemy2 = Enemy(200, 250)
enemy3 = Enemy(300, 400)

enemy_group.add(enemy1, enemy2, enemy3)

# --- Main Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update positions
    enemy_group.update()

    # Draw everything
    screen.fill((0, 0, 0)) # Clear screen with black
    enemy_group.draw(screen) # Draw all enemies
    
    pygame.display.flip()
    clock.tick(60) # 60 Frames per second