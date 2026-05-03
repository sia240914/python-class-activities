import pygame

pygame.init()
screen=pygame.display.set_mode((400,300))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(150,0,125),pygame.Rect(100,30,90,89))
    pygame.display.flip()