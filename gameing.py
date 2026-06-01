import pygame


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 60


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame Screen")


clock = pygame.time.Clock()


BACKGROUND_COLOR = (40, 44, 52)  


running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill(BACKGROUND_COLOR)  
    
    pygame.display.flip()

    
    clock.tick(FRAME_RATE)


pygame.quit()

