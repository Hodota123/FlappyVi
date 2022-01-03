import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
WHITE=(255,255,255)
x_bird=50
y_bird=350
tube1_x=0
tube2_x=200
tube3_x=400
tube_width=50
tube1_height=randint(400,1200)
tube2_height=randint(400,1200)
tube3_height=randint(400,1200)
d_2tube=150
bird_drop_velocity=0
gravity=0.5
tube_velocity=2
background_img=pygame.image.load('background2.jpg')
background_img=pygame.transform.scale(background_img,(400,600))
bird_img=pygame.image.load('bird.png')
bird_img=pygame.transform.scale(bird_img,(80,80))
tube_img=pygame.image.load('colunm.png')
running=True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    screen.blit(background_img,(0,0))
    # ép ảnh ống và vẽ ống
    tube1_img=pygame.transform.scale(tube_img,(tube_width,tube1_height))
    tube1=screen.blit(tube1_img,(tube1_x,0))
    tube2_img=pygame.transform.scale(tube_img,(tube_width,tube2_height))
    tube2=screen.blit(tube2_img,(tube2_x,0))
    tube3_img=pygame.transform.scale(tube_img,(tube_width,tube3_height))
    tube3=screen.blit(tube3_img,(tube3_x,0))
# ống di chuyển sang trái
    tube1_x=tube1_x-tube_velocity
    tube2_x=tube2_x-tube_velocity
    tube3_x=tube3_x-tube_velocity
# tạo ống mới
    if tube1_x< - tube_width:
     tube1_x=550
     tube1_height=randint(600,800)    
    if tube2_x< - tube_width:
     tube2_x=550
     tube2_height=randint(600,800) 
    if tube3_x< - tube_width:
     tube3_x=550
     tube3_height=randint(600,800)  
# vẽ chim
    bird=screen.blit(bird_img,(x_bird,y_bird))
#chim rơi
    y_bird=y_bird + bird_drop_velocity
    bird_drop_velocity=bird_drop_velocity+ gravity
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bird_drop_velocity=0
                bird_drop_velocity=bird_drop_velocity-7 
    pygame.display.flip()
pygame.quit()



