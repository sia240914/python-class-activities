i.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit=False
        if self.rect.left <=0 or self.rect.right >=500 :
            self.velocity[0]=-self.velocity[0]
            boundry_hit=True
        if self.rect.top <=0 or self.rect.bottom >=400 :
            self.velocity[1]=-self.velocity[1]
            boundry_hit=True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def color_change(self):
        self.image.fill(random.choice([MAGENTA,GREEN,BLACK,RED]))

def bg_color_change():
        global bg_color
        bg_color=random.choice([BLUE,PURPLE,PINK])
      

all_sprite_list=pygame.sprite.Group()
sp1=Sprite(BLUE,50,60)
sp1.rect.x=random.randint(0,500)
sp1.rect.y=random.randint(0,370)
all_sprite_list.add(sp1)

screen=pygame.display.set_mode((550,400))
pygame.display.set_caption("boundry sprite")
bg_color=BLUE
screen.fill(bg_color)
 
exit=False
clock=pygame.time.Clock()


while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit=True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.color_change()

        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            bg_color_change()

    all_sprite_list.update()
    screen.fill(bg_color)mport pygame 

import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT+2
BLUE=pygame.Color('blue')
PURPLE=pygame.Color('purple')
PINK=pygame.Color('pink')

MAGENTA=pygame.Color('magenta')
BLACK=pygame.Color('black')
GREEN=pygame.Color('green')
RED=pygame.Color('red')

class Sprite(pygame
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)
pygame.quit()

















































