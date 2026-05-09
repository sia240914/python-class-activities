import pygame

pygame.init()
screen=pygame.display.set_mode((500,400))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,20,87),pygame.Rect(150,30,130,95))
    pygame.display.flip()