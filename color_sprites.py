import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fixed Time Step Sprite Example")
clock = pygame.time.Clock()

class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = self.get_random_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed  

    def get_random_color(self):
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    def change_color(self):
        self.color = self.get_random_color()
        self.image.fill(self.color)

    def update(self):
        """Move the sprite down. No DT math needed here!"""
        self.rect.y += self.speed
        
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height

sprite1 = CustomSprite(200, 100, 100, 100, speed=3)
sprite2 = CustomSprite(500, 100, 100, 100, speed=3)

all_sprites = pygame.sprite.Group(sprite1, sprite2)


TIME_PER_FRAME = 16.666  
accumulator = 0.0

running = True
while running:
    
    dt_ms = clock.tick()
    accumulator += dt_ms

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))
        elif event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    
    while accumulator >= TIME_PER_FRAME:
        all_sprites.update()    
        accumulator -= TIME_PER_FRAME

    
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
