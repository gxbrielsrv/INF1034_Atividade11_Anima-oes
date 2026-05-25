import pygame, sys 
from pygame.locals import QUIT
from pygame.locals import *
clock = pygame.time.Clock()
current_frame = 0
anim_time = 0
run_animation = False



#dog_img  = pygame.image.load('')
current_frame_sp = 0
anim_time_sp = 0
megaman_spritesheet = pygame.image.load('megaman_spritesheet.png')
walk_spritesheet = pygame.image.load('walk.png')



hero_img = pygame.image.load(('Nova pasta/Hero_Walk_01.png'))

hero_walk_list = []
for i in range(4):
    hero_walk_list.append(pygame.image.load(f'Nova pasta/Hero_Walk_0{i+1}.png'))

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                run_animation = True



        
    clock.tick(60)
    dt = clock.get_time()
    
    anim_time += dt
    anim_time_sec = anim_time/1000

    if run_animation:
        anim_time_sp += dt
        anim_time_sp_sec = anim_time_sp / 1000
        if anim_time_sp_sec >0.1:
            current_frame_sp +=1
            if current_frame_sp > 9:
                run_animation = False
            anim_time_sp = 0





    if anim_time_sec > 0.18:
        current_frame += 1
        if current_frame > len(hero_walk_list) - 1:
            current_frame = 0
        anim_time = 0
    
    
    screen.fill((255,255,255))


    screen.blit(hero_walk_list[current_frame], (0, 0))


    # if current_frame_sp < 5:
    #     screen.blit(megaman_spritesheet,(200,200),(60 * current_frame_sp,0,60,60))
    # else:
    #     screen.blit(megaman_spritesheet,(200,200),(60 * [current_frame_sp - 5],60,60,60))




    screen.blit(megaman_spritesheet,(200,200),(60 * (current_frame_sp%5),60* (current_frame // 5),60,60))



    pygame.display.update()
