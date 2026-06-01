import pygame


pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (RGB)
BG_COLOR = (30, 30, 30)
BLUE = (0, 128, 255)
RED = (255, 100, 100)

# Setup the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites Game")

class BoxSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5


    def handle_keys(self):
        """Checks for key presses to move this specific sprite."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(SCREEN_WIDTH, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(SCREEN_HEIGHT, self.rect.bottom)


player = BoxSprite(BLUE, 100, 250, 50, 50)

static_target = BoxSprite(RED, 600, 250, 60, 80)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(static_target)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    player.handle_keys()

    
    screen.fill(BG_COLOR)          
    all_sprites.draw(screen)       
    pygame.display.flip()         


pygame.quit()
