import math
import random
import pygame



SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=10
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27

pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
bg=pygame.image.load('download.jpeg')

pygame.display.set_caption("space invader")
icon=pygame.image.load('download__1_-removebg-preview.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('download__1_-removebg-preview.png')
player_x=PLAYER_START_X
player_y=PLAYER_START_Y
player_x_change=0





















running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

pygame.quit()


