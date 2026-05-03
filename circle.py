import pygame

pygame.init()
screen=pygame.display.set_mode((400,300))
screen.fill((208,230,52))
BLACK=(0,0,0)
pygame.draw.circle(screen, BLACK ,(100,100),50)
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(150,0,125),pygame.Rect(100,30,90,89))
    pygame.display.flip()