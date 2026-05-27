import pygame, sys 
from pygame.locals import QUIT
from pygame.locals import *

clock = pygame.time.Clock()

current_frame = 0
anim_time = 0

run_animation = False
olhar_direita = True
jump_animation = False

current_frame_sp = 0
anim_time_sp = 0

current_frame_jump = 0
anim_time_jump = 0


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World')

run_spritesheet = pygame.image.load('Knight 2D Pixel Art/Sprites/without_outline/RUN.png')
jump_spritesheet = pygame.image.load('Knight 2D Pixel Art/Sprites/without_outline/JUMP.png')

walk_png_list = []
for i in range(8):
    walk_png_list.append(pygame.image.load(f'PNG_sequence/walkL{i+1}.png'))



frame_width = 95
jump_max_frames = jump_spritesheet.get_width() // frame_width
run_max_frames = run_spritesheet.get_width() // frame_width


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        run_animation = True
        olhar_direita = True

    if keys[pygame.K_a]:
        run_animation = True
        olhar_direita = False

    if keys[pygame.K_SPACE]:
        jump_animation = True
        current_frame_jump = 0


    dt = clock.tick(60)


    
    if run_animation:
        anim_time_sp += dt

        if anim_time_sp / 1000 > 0.1:
            current_frame_sp += 1

            if current_frame_sp >= run_max_frames:
                current_frame_sp = 0
                run_animation = False

            anim_time_sp = 0


    
    anim_time += dt
    if anim_time > 180:
        current_frame += 1
        if current_frame > len(walk_png_list) - 1:
            current_frame = 0
        anim_time = 0


    
    if jump_animation:
        anim_time_jump += dt

        if anim_time_jump / 1000 > 0.08:
            current_frame_jump += 1

            if current_frame_jump >= jump_max_frames:
                current_frame_jump = jump_max_frames - 1
                jump_animation = False

            anim_time_jump = 0


    screen.fill((255,255,255))

    screen.blit(walk_png_list[current_frame], (0, 0))


   
    frame = run_spritesheet.subsurface(
        (frame_width * current_frame_sp, 0, frame_width, 64)
    )

    if not olhar_direita:
        frame = pygame.transform.flip(frame, True, False)

    frame = pygame.transform.scale(frame, (180, 240))


    
    if jump_animation:
        frame2 = jump_spritesheet.subsurface((frame_width * current_frame_jump, 0, frame_width, 64))
        if not olhar_direita:
            frame2 = pygame.transform.flip(frame2, True, False)
        frame2 = pygame.transform.scale(frame2, (180, 240))
        screen.blit(frame2, (200, 200))
    else:
        screen.blit(frame, (200, 200))


    pygame.display.update()